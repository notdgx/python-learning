import React, { useState } from 'react';
import { FileCode, Play } from '@phosphor-icons/react';
import { ReferenceFile } from '../../types/content';
import { getReferenceFileContent } from '../../services/contentService';
import { CodeViewerModal } from './CodeViewerModal';

interface ReferenceFileListProps {
  references: ReferenceFile[];
}

export const ReferenceFileList: React.FC<ReferenceFileListProps> = ({ references }) => {
  const [selectedFile, setSelectedFile] = useState<{ name: string; code: string } | null>(null);

  if (!references || references.length === 0) {
    return null;
  }

  const handleOpenCode = (ref: ReferenceFile) => {
    const code = getReferenceFileContent(ref.sourcePath);
    setSelectedFile({ name: ref.name, code });
  };

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '10px', marginTop: '24px', paddingTop: '18px', borderTop: '1px solid var(--color-hairline)' }}>
      <div
        style={{
          display: 'flex',
          alignItems: 'center',
          gap: '6px',
          fontSize: '12px',
          fontWeight: 600,
          color: 'var(--color-mute)',
          textTransform: 'uppercase',
          letterSpacing: '0.06em'
        }}
      >
        <FileCode size={15} />
        <span>Reference Files ({references.length})</span>
      </div>

      <div style={{ display: 'flex', flexDirection: 'column', gap: '6px' }}>
        {references.map((ref) => (
          <button
            key={ref.name}
            type="button"
            onClick={() => handleOpenCode(ref)}
            style={{
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'space-between',
              padding: '6px 10px',
              backgroundColor: 'var(--color-surface)',
              border: '1px solid var(--color-hairline)',
              borderRadius: 'var(--radius-sm)',
              color: 'var(--color-ink)',
              fontSize: '12.5px',
              fontFamily: 'var(--font-mono)',
              textAlign: 'left',
              cursor: 'pointer',
              transition: 'all 0.15s ease'
            }}
            onMouseEnter={(e) => {
              e.currentTarget.style.borderColor = 'var(--color-hairline-strong)';
              e.currentTarget.style.backgroundColor = 'var(--color-surface-elevated)';
            }}
            onMouseLeave={(e) => {
              e.currentTarget.style.borderColor = 'var(--color-hairline)';
              e.currentTarget.style.backgroundColor = 'var(--color-surface)';
            }}
          >
            <span style={{ overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>
              {ref.name}
            </span>
            <Play size={10} color="var(--color-mute)" />
          </button>
        ))}
      </div>

      {selectedFile && (
        <CodeViewerModal
          filename={selectedFile.name}
          code={selectedFile.code}
          isOpen={true}
          onClose={() => setSelectedFile(null)}
        />
      )}
    </div>
  );
};
