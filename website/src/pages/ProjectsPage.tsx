import React from 'react';
import { Code } from '@phosphor-icons/react';
import { EmptyState } from '../components/common/EmptyState';

export const ProjectsPage: React.FC = () => {
  return (
    <div style={{ maxWidth: 'var(--max-content-width)', margin: '0 auto', padding: '48px 24px 80px', width: '100%' }}>
      <div style={{ marginBottom: '36px' }}>
        <span style={{ fontSize: '12px', fontWeight: 600, color: 'var(--color-mute)', textTransform: 'uppercase', letterSpacing: '0.08em' }}>
          Portfolio
        </span>
        <h1 style={{ fontSize: '2.4rem', color: 'var(--color-ink)', marginTop: '4px', marginBottom: '8px' }}>
          Python Projects
        </h1>
        <p style={{ fontSize: '15px', color: 'var(--color-mute)', maxWidth: '650px' }}>
          Hands-on Python architectures, command-line tools, automation scripts, and systems projects.
        </p>
      </div>

      <EmptyState
        title="Projects Pipeline Expanding"
        description="Active project implementations will be indexed here directly from repository source files in an upcoming iteration."
        actionText="Explore Python Notes"
        onAction={() => window.location.assign('/notes')}
        icon={<Code size={48} weight="thin" color="var(--color-stone)" />}
      />
    </div>
  );
};
