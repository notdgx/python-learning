import rawMetadata from '../../../notes/metadata.json';
import { MetadataFile, NoteDocument, TopicMetadata } from '../types/content';

const metadata = rawMetadata as unknown as MetadataFile;

// Eagerly glob all markdown files from notes/
const markdownFiles = import.meta.glob('../../../notes/**/*.md', {
  query: '?raw',
  import: 'default',
  eager: true
}) as Record<string, string>;

// Eagerly glob all python reference files from notes/
const pythonFiles = import.meta.glob('../../../notes/**/*.py', {
  query: '?raw',
  import: 'default',
  eager: true
}) as Record<string, string>;

/**
 * Normalizes a route string for comparison (stripping leading/trailing slashes, lowercasing)
 */
function normalizeRoute(route: string): string {
  let clean = route.trim().toLowerCase();
  if (!clean.startsWith('/')) clean = '/' + clean;
  if (clean.length > 1 && clean.endsWith('/')) clean = clean.slice(0, -1);
  return clean;
}

/**
 * Resolves raw markdown content by matching note.sourcePath
 */
function findMarkdownContent(sourcePath: string): string {
  // sourcePath is e.g. "notes/00-Basics/00-Intro-and-Internal-Working/00-LowLevelExecution.md"
  const normalizedTarget = '/' + sourcePath.replace(/^\/+/, '');
  
  for (const [key, content] of Object.entries(markdownFiles)) {
    if (key.toLowerCase() === normalizedTarget.toLowerCase() || key.endsWith(sourcePath)) {
      return content;
    }
  }

  // Fallback match by filename
  const filename = sourcePath.split('/').pop();
  if (filename) {
    for (const [key, content] of Object.entries(markdownFiles)) {
      if (key.endsWith('/' + filename)) {
        return content;
      }
    }
  }

  return '';
}

/**
 * Resolves python reference file content by name and note source directory
 */
export function getReferenceFileContent(sourcePath: string): string {
  const normalizedTarget = '/' + sourcePath.replace(/^\/+/, '');

  for (const [key, content] of Object.entries(pythonFiles)) {
    if (key.toLowerCase() === normalizedTarget.toLowerCase() || key.endsWith(sourcePath)) {
      return content;
    }
  }
  return '';
}

/**
 * Returns the entire topic tree metadata
 */
export function getTopicTree(): TopicMetadata[] {
  return metadata.sections.notes.topics || [];
}

/**
 * Returns all notes in a flat list with topic context
 */
export function getAllNotes(): NoteDocument[] {
  const list: NoteDocument[] = [];
  const topics = getTopicTree();

  for (const topic of topics) {
    for (const subtopic of topic.subtopics) {
      for (const note of subtopic.notes) {
        const raw = findMarkdownContent(note.sourcePath);
        list.push({
          metadata: note,
          rawContent: raw,
          topicTitle: topic.title,
          subtopicTitle: subtopic.title,
          topicSlug: topic.slug,
          subtopicSlug: subtopic.slug
        });
      }
    }
  }

  return list;
}

/**
 * Finds a note by route
 */
export function getNoteByRoute(route: string): NoteDocument | null {
  const target = normalizeRoute(route);
  const all = getAllNotes();

  // 1. Exact route match
  const exact = all.find((n) => normalizeRoute(n.metadata.route) === target);
  if (exact) return exact;

  // 2. Match by ending slug
  const slug = target.split('/').pop();
  if (slug) {
    const slugMatch = all.find((n) => {
      const noteSlug = n.metadata.route.split('/').pop();
      return noteSlug === slug;
    });
    if (slugMatch) return slugMatch;
  }

  // 3. Fallback: match by ID
  const idMatch = all.find((n) => n.metadata.id === route);
  if (idMatch) return idMatch;

  return null;
}

/**
 * Returns previous and next notes for navigation
 */
export function getAdjacentNotes(currentRoute: string): { prev: NoteDocument | null; next: NoteDocument | null } {
  const all = getAllNotes();
  const index = all.findIndex((n) => normalizeRoute(n.metadata.route) === normalizeRoute(currentRoute));

  if (index === -1) {
    return { prev: null, next: null };
  }

  return {
    prev: index > 0 ? all[index - 1] : null,
    next: index < all.length - 1 ? all[index + 1] : null
  };
}

/**
 * Full-text and heading search across notes
 */
export function searchNotes(query: string): Array<{
  note: NoteDocument;
  matchType: 'title' | 'heading' | 'topic' | 'content';
  snippet: string;
}> {
  const q = query.trim().toLowerCase();
  if (!q) return [];

  const results: Array<{
    note: NoteDocument;
    matchType: 'title' | 'heading' | 'topic' | 'content';
    snippet: string;
  }> = [];

  const all = getAllNotes();

  for (const doc of all) {
    // 1. Title match
    if (doc.metadata.title.toLowerCase().includes(q)) {
      results.push({
        note: doc,
        matchType: 'title',
        snippet: doc.metadata.title
      });
      continue;
    }

    // 2. Topic/subtopic match
    if (doc.topicTitle.toLowerCase().includes(q) || doc.subtopicTitle.toLowerCase().includes(q)) {
      results.push({
        note: doc,
        matchType: 'topic',
        snippet: `${doc.topicTitle} → ${doc.subtopicTitle}`
      });
      continue;
    }

    // 3. Heading match
    const matchingHeading = doc.metadata.headings.find((h) => h.text.toLowerCase().includes(q));
    if (matchingHeading) {
      results.push({
        note: doc,
        matchType: 'heading',
        snippet: matchingHeading.text
      });
      continue;
    }

    // 4. Content match
    const contentLower = doc.rawContent.toLowerCase();
    const pos = contentLower.indexOf(q);
    if (pos !== -1) {
      const start = Math.max(0, pos - 40);
      const end = Math.min(doc.rawContent.length, pos + q.length + 40);
      const snippet = '...' + doc.rawContent.slice(start, end).replace(/\n/g, ' ') + '...';
      results.push({
        note: doc,
        matchType: 'content',
        snippet
      });
    }
  }

  return results;
}

/**
 * Returns metadata stats
 */
export function getStats() {
  return metadata.stats;
}
