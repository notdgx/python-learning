import React, { useState } from 'react';
import { Link, useLocation } from 'react-router-dom';
import { CaretDown, CaretRight, BookOpen, SidebarSimple } from '@phosphor-icons/react';
import { TopicMetadata } from '../../types/content';

interface TopicSidebarProps {
  topics: TopicMetadata[];
  isOpen: boolean;
  onToggle: () => void;
}

export const TopicSidebar: React.FC<TopicSidebarProps> = ({
  topics,
  isOpen,
  onToggle
}) => {
  const location = useLocation();
  const [collapsedSections, setCollapsedSections] = useState<Record<string, boolean>>({});

  const toggleSection = (id: string) => {
    setCollapsedSections((prev) => ({ ...prev, [id]: !prev[id] }));
  };

  const isNoteActive = (route: string) => {
    return location.pathname.toLowerCase() === route.toLowerCase();
  };

  if (!isOpen) {
    return (
      <button
        onClick={onToggle}
        style={{
          position: 'fixed',
          left: '16px',
          bottom: '24px',
          zIndex: 100,
          display: 'flex',
          alignItems: 'center',
          gap: '8px',
          padding: '8px 14px',
          backgroundColor: 'var(--color-surface-elevated)',
          border: '1px solid var(--color-hairline-strong)',
          borderRadius: 'var(--radius-full)',
          color: 'var(--color-ink)',
          fontSize: '13px',
          fontWeight: 500,
          boxShadow: '0 8px 24px rgba(0,0,0,0.6)'
        }}
        aria-label="Show topic navigation"
      >
        <SidebarSimple size={16} />
        <span>Topics</span>
      </button>
    );
  }

  return (
    <aside
      style={{
        width: 'var(--sidebar-width)',
        flexShrink: 0,
        height: 'calc(100vh - var(--navbar-height))',
        position: 'sticky',
        top: 'var(--navbar-height)',
        overflowY: 'auto',
        borderRight: '1px solid var(--color-hairline)',
        backgroundColor: 'var(--color-canvas)',
        padding: '24px 16px',
        display: 'flex',
        flexDirection: 'column',
        gap: '20px'
      }}
      aria-label="Topic navigation"
    >
      {/* Sidebar Header */}
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', paddingBottom: '12px', borderBottom: '1px solid var(--color-hairline-soft)' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px', color: 'var(--color-ink)', fontWeight: 600, fontSize: '14px' }}>
          <BookOpen size={18} color="var(--color-mute)" />
          <span>Python Learning</span>
        </div>
        <button
          onClick={onToggle}
          style={{
            padding: '4px',
            color: 'var(--color-mute)',
            borderRadius: 'var(--radius-xs)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center'
          }}
          title="Hide sidebar"
          aria-label="Hide sidebar"
        >
          <SidebarSimple size={16} />
        </button>
      </div>

      {/* Topic Hierarchy */}
      <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
        {topics.map((topic) => (
          <div key={topic.id} style={{ display: 'flex', flexDirection: 'column', gap: '6px' }}>
            {/* Level 2: Topic Title */}
            <div
              style={{
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'space-between',
                padding: '4px 8px',
                fontSize: '12px',
                fontWeight: 600,
                color: 'var(--color-mute)',
                textTransform: 'uppercase',
                letterSpacing: '0.06em'
              }}
            >
              <span>{topic.title}</span>
            </div>

            {/* Level 3: Subtopics */}
            <div style={{ display: 'flex', flexDirection: 'column', gap: '4px', paddingLeft: '4px' }}>
              {topic.subtopics.map((subtopic) => {
                const isCollapsed = !!collapsedSections[subtopic.id];

                return (
                  <div key={subtopic.id} style={{ display: 'flex', flexDirection: 'column', gap: '2px' }}>
                    <button
                      type="button"
                      onClick={() => toggleSection(subtopic.id)}
                      style={{
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'space-between',
                        width: '100%',
                        padding: '6px 8px',
                        borderRadius: 'var(--radius-sm)',
                        fontSize: '13.5px',
                        fontWeight: 500,
                        color: 'var(--color-ink)',
                        backgroundColor: 'transparent',
                        textAlign: 'left',
                        transition: 'background-color 0.15s ease'
                      }}
                      onMouseEnter={(e) => (e.currentTarget.style.backgroundColor = 'var(--color-surface)')}
                      onMouseLeave={(e) => (e.currentTarget.style.backgroundColor = 'transparent')}
                    >
                      <span style={{ overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>
                        {subtopic.title}
                      </span>
                      {isCollapsed ? (
                        <CaretRight size={12} color="var(--color-stone)" />
                      ) : (
                        <CaretDown size={12} color="var(--color-stone)" />
                      )}
                    </button>

                    {/* Level 4: Notes */}
                    {!isCollapsed && (
                      <div
                        style={{
                          display: 'flex',
                          flexDirection: 'column',
                          gap: '1px',
                          paddingLeft: '14px',
                          borderLeft: '1px solid var(--color-hairline)',
                          marginLeft: '12px',
                          marginTop: '2px',
                          marginBottom: '6px'
                        }}
                      >
                        {subtopic.notes.map((note) => {
                          const active = isNoteActive(note.route);

                          return (
                            <Link
                              key={note.id}
                              to={note.route}
                              style={{
                                display: 'block',
                                padding: '6px 10px',
                                borderRadius: 'var(--radius-xs)',
                                fontSize: '13px',
                                color: active ? 'var(--color-on-dark)' : 'var(--color-body)',
                                backgroundColor: active ? 'var(--color-surface-card)' : 'transparent',
                                fontWeight: active ? 500 : 400,
                                borderLeft: active ? '2px solid var(--color-primary)' : '2px solid transparent',
                                transition: 'all 0.15s ease',
                                overflow: 'hidden',
                                textOverflow: 'ellipsis',
                                whiteSpace: 'nowrap'
                              }}
                            >
                              {note.title}
                            </Link>
                          );
                        })}
                      </div>
                    )}
                  </div>
                );
              })}
            </div>
          </div>
        ))}
      </div>
    </aside>
  );
};
