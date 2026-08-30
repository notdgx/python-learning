import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { MagnifyingGlass, BookOpen, ArrowRight, FileText } from '@phosphor-icons/react';
import { getTopicTree, searchNotes } from '../services/contentService';

export const NotesExplorerPage: React.FC = () => {
  const [searchQuery, setSearchQuery] = useState('');
  const topics = getTopicTree();

  const searchResults = searchQuery.trim() ? searchNotes(searchQuery) : [];

  return (
    <div style={{ maxWidth: 'var(--max-content-width)', margin: '0 auto', padding: '48px 24px 80px', width: '100%' }}>
      {/* Header */}
      <div style={{ marginBottom: '36px' }}>
        <span style={{ fontSize: '12px', fontWeight: 600, color: 'var(--color-mute)', textTransform: 'uppercase', letterSpacing: '0.08em' }}>
          Curriculum
        </span>
        <h1 style={{ fontSize: '2.4rem', color: 'var(--color-ink)', marginTop: '4px', marginBottom: '8px' }}>
          Python Learning Notes
        </h1>
        <p style={{ fontSize: '15px', color: 'var(--color-mute)', maxWidth: '650px' }}>
          Explore structured notes on Python syntax, low-level bytecode, object models, symbol tables, and internal architecture.
        </p>

        {/* Search Bar */}
        <div style={{ marginTop: '24px', position: 'relative', maxWidth: '520px' }}>
          <MagnifyingGlass
            size={18}
            color="var(--color-mute)"
            style={{ position: 'absolute', left: '14px', top: '50%', transform: 'translateY(-50%)' }}
          />
          <input
            type="text"
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            placeholder="Search notes, topics, or concepts..."
            style={{
              width: '100%',
              height: '42px',
              padding: '0 16px 0 42px',
              backgroundColor: 'var(--color-surface-elevated)',
              border: '1px solid var(--color-hairline)',
              borderRadius: 'var(--radius-md)',
              color: 'var(--color-on-dark)',
              fontSize: '14px',
              outline: 'none',
              fontFamily: 'inherit',
              transition: 'border-color 0.15s ease'
            }}
            onFocus={(e) => (e.currentTarget.style.borderColor = 'var(--color-hairline-strong)')}
            onBlur={(e) => (e.currentTarget.style.borderColor = 'var(--color-hairline)')}
            aria-label="Search notes"
          />
        </div>
      </div>

      {/* Search Results if query exists */}
      {searchQuery.trim() ? (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
          <div style={{ fontSize: '13px', color: 'var(--color-mute)' }}>
            Found {searchResults.length} matching result{searchResults.length === 1 ? '' : 's'} for &ldquo;{searchQuery}&rdquo;
          </div>

          {searchResults.length === 0 ? (
            <div style={{ padding: '3rem 1.5rem', textAlign: 'center', background: 'var(--color-surface)', borderRadius: 'var(--radius-lg)', border: '1px dashed var(--color-hairline)' }}>
              <p style={{ color: 'var(--color-mute)', fontSize: '14px' }}>No notes found matching your search term.</p>
            </div>
          ) : (
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(320px, 1fr))', gap: '16px' }}>
              {searchResults.map(({ note, matchType, snippet }) => (
                <Link
                  key={note.metadata.id}
                  to={note.metadata.route}
                  className="surface-card"
                  style={{ display: 'flex', flexDirection: 'column', gap: '8px', padding: '18px' }}
                >
                  <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
                    <span style={{ fontSize: '11px', color: 'var(--color-ash)', textTransform: 'uppercase' }}>
                      {note.topicTitle} → {note.subtopicTitle}
                    </span>
                    <span style={{ fontSize: '11px', padding: '2px 6px', backgroundColor: 'var(--color-surface-elevated)', borderRadius: 'var(--radius-xs)', color: 'var(--color-mute)' }}>
                      {matchType}
                    </span>
                  </div>
                  <h3 style={{ fontSize: '15px', color: 'var(--color-ink)', fontWeight: 500 }}>
                    {note.metadata.title}
                  </h3>
                  <p style={{ fontSize: '12.5px', color: 'var(--color-mute)', lineClamp: 2, overflow: 'hidden', display: '-webkit-box', WebkitLineClamp: 2, WebkitBoxOrient: 'vertical' }}>
                    {snippet}
                  </p>
                </Link>
              ))}
            </div>
          )}
        </div>
      ) : (
        /* Full Topic Roadmap */
        <div style={{ display: 'flex', flexDirection: 'column', gap: '40px' }}>
          {topics.map((topic) => (
            <div key={topic.id} style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
              {/* Topic Header */}
              <div style={{ display: 'flex', alignItems: 'center', gap: '10px', paddingBottom: '10px', borderBottom: '1px solid var(--color-hairline)' }}>
                <BookOpen size={22} color="var(--color-ink)" />
                <h2 style={{ fontSize: '1.45rem', color: 'var(--color-ink)' }}>
                  {topic.title}
                </h2>
              </div>

              {/* Subtopics Grid */}
              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(320px, 1fr))', gap: '20px' }}>
                {topic.subtopics.map((subtopic) => (
                  <div
                    key={subtopic.id}
                    className="surface-card"
                    style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}
                  >
                    <div>
                      <h3 style={{ fontSize: '1.15rem', color: 'var(--color-ink)', marginBottom: '4px' }}>
                        {subtopic.title}
                      </h3>
                      <span style={{ fontSize: '12px', color: 'var(--color-mute)' }}>
                        {subtopic.notes.length} note{subtopic.notes.length === 1 ? '' : 's'} in this module
                      </span>
                    </div>

                    <div style={{ display: 'flex', flexDirection: 'column', gap: '6px' }}>
                      {subtopic.notes.map((note) => (
                        <Link
                          key={note.id}
                          to={note.route}
                          style={{
                            display: 'flex',
                            alignItems: 'center',
                            justifyContent: 'space-between',
                            padding: '8px 12px',
                            backgroundColor: 'var(--color-surface-card)',
                            border: '1px solid var(--color-hairline)',
                            borderRadius: 'var(--radius-sm)',
                            color: 'var(--color-ink)',
                            fontSize: '13.5px',
                            transition: 'all 0.15s ease'
                          }}
                          onMouseEnter={(e) => {
                            e.currentTarget.style.borderColor = 'var(--color-hairline-strong)';
                            e.currentTarget.style.backgroundColor = 'var(--color-surface-elevated)';
                          }}
                          onMouseLeave={(e) => {
                            e.currentTarget.style.borderColor = 'var(--color-hairline)';
                            e.currentTarget.style.backgroundColor = 'var(--color-surface-card)';
                          }}
                        >
                          <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                            <FileText size={15} color="var(--color-mute)" />
                            <span>{note.title}</span>
                          </div>
                          <ArrowRight size={12} color="var(--color-stone)" />
                        </Link>
                      ))}
                    </div>
                  </div>
                ))}
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};
