export interface Heading {
  id: string;
  text: string;
  level: number;
}

export interface ReferenceFile {
  name: string;
  sourcePath: string;
  order: number;
  referenceIndex: number;
  sha256: string;
  sizeBytes: number;
  content?: string;
}

export interface NoteMetadata {
  id: string;
  title: string;
  route: string;
  sourcePath: string;
  order: number;
  date: string;
  time: string;
  headings: Heading[];
  references: ReferenceFile[];
  sha256: string;
  sizeBytes: number;
}

export interface SubtopicMetadata {
  id: string;
  title: string;
  order: number;
  slug: string;
  notes: NoteMetadata[];
}

export interface TopicMetadata {
  id: string;
  title: string;
  order: number;
  slug: string;
  subtopics: SubtopicMetadata[];
}

export interface MetadataFile {
  schemaVersion: number;
  generatedAt: string;
  contentRoot: string;
  sections: {
    notes: {
      id: string;
      title: string;
      topics: TopicMetadata[];
    };
  };
  stats: {
    topics: number;
    subtopics: number;
    notes: number;
    referenceFiles: number;
  };
}

export interface NoteDocument {
  metadata: NoteMetadata;
  rawContent: string;
  topicTitle: string;
  subtopicTitle: string;
  topicSlug: string;
  subtopicSlug: string;
}

export interface NavItem {
  id: string;
  title: string;
  route: string;
  type: 'topic' | 'subtopic' | 'note';
  children?: NavItem[];
}
