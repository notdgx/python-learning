import React from 'react';
import { Link } from 'react-router-dom';
import { CaretRight } from '@phosphor-icons/react';

interface BreadcrumbsProps {
  topicTitle: string;
  subtopicTitle: string;
  noteTitle: string;
}

export const Breadcrumbs: React.FC<BreadcrumbsProps> = ({
  topicTitle,
  subtopicTitle,
  noteTitle
}) => {
  return (
    <nav
      aria-label="Breadcrumbs"
      className="breadcrumbs-nav"
      style={{
        display: 'flex',
        alignItems: 'center',
        gap: '6px',
        fontSize: '12.5px',
        color: 'var(--color-mute)',
        marginBottom: '1.25rem',
        overflowX: 'auto',
        whiteSpace: 'nowrap',
        WebkitOverflowScrolling: 'touch',
        scrollbarWidth: 'none',
        paddingBottom: '2px'
      }}
    >
      <Link to="/notes" style={{ color: 'var(--color-mute)', transition: 'color 0.15s ease', flexShrink: 0 }}>
        Python Learning
      </Link>
      <CaretRight size={12} color="var(--color-stone)" style={{ flexShrink: 0 }} />
      <span style={{ color: 'var(--color-charcoal)', flexShrink: 0 }}>{topicTitle}</span>
      <CaretRight size={12} color="var(--color-stone)" style={{ flexShrink: 0 }} />
      <span style={{ color: 'var(--color-charcoal)', flexShrink: 0 }}>{subtopicTitle}</span>
      <CaretRight size={12} color="var(--color-stone)" style={{ flexShrink: 0 }} />
      <span style={{ color: 'var(--color-ink)', fontWeight: 500, flexShrink: 0 }}>{noteTitle}</span>
    </nav>
  );
};
