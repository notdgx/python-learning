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
      style={{
        display: 'flex',
        alignItems: 'center',
        gap: '6px',
        fontSize: '13px',
        color: 'var(--color-mute)',
        flexWrap: 'wrap',
        marginBottom: '1.5rem'
      }}
    >
      <Link to="/notes" style={{ color: 'var(--color-mute)', transition: 'color 0.15s ease' }}>
        Python Learning
      </Link>
      <CaretRight size={12} color="var(--color-stone)" />
      <span style={{ color: 'var(--color-charcoal)' }}>{topicTitle}</span>
      <CaretRight size={12} color="var(--color-stone)" />
      <span style={{ color: 'var(--color-charcoal)' }}>{subtopicTitle}</span>
      <CaretRight size={12} color="var(--color-stone)" />
      <span style={{ color: 'var(--color-ink)', fontWeight: 500 }}>{noteTitle}</span>
    </nav>
  );
};
