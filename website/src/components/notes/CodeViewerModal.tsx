import React, { useEffect, useState } from 'react';
import { X, Copy, Check, DownloadSimple, FileCode } from '@phosphor-icons/react';
import { highlightCode } from '../../utils/markdown';

interface CodeViewerModalProps {
  filename: string;
  code: string;
  isOpen: boolean;
  onClose: () => void;
}

export const CodeViewerModal: React.FC<CodeViewerModalProps> = ({
  filename,
  code,
  isOpen,
  onClose
}) => {
  const [copied, setCopied] = useState(false);

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape' && isOpen) {
        onClose();
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [isOpen, onClose]);

  if (!isOpen) return null;

  const handleCopy = async () => {
    try {
      await navigator.clipboard.writeText(code);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    } catch {
      setCopied(false);
    }
  };

  const handleDownload = () => {
    const blob = new Blob([code], { type: 'text/x-python;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = filename;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    URL.revokeObjectURL(url);
  };

  const highlightedHtml = highlightCode(code, 'python');

  return (
    <div
      style={{
        position: 'fixed',
        inset: 0,
        zIndex: 9999,
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        padding: '12px',
        backgroundColor: 'rgba(0, 0, 0, 0.85)',
        backdropFilter: 'blur(12px)',
        WebkitBackdropFilter: 'blur(12px)'
      }}
      onClick={(e) => {
        if (e.target === e.currentTarget) onClose();
      }}
      role="dialog"
      aria-modal="true"
      aria-labelledby="code-viewer-title"
    >
      <div
        style={{
          width: '100%',
          maxWidth: '860px',
          maxHeight: '88vh',
          backgroundColor: 'var(--color-surface)',
          border: '1px solid var(--color-hairline-strong)',
          borderRadius: 'var(--radius-lg)',
          boxShadow: '0 24px 48px rgba(0, 0, 0, 0.95)',
          display: 'flex',
          flexDirection: 'column',
          overflow: 'hidden'
        }}
      >
        {/* Header Bar */}
        <div
          style={{
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'space-between',
            padding: '10px 14px',
            backgroundColor: 'var(--color-surface-elevated)',
            borderBottom: '1px solid var(--color-hairline)',
            gap: '8px'
          }}
        >
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px', minWidth: 0 }}>
            <FileCode size={18} color="var(--color-mute)" style={{ flexShrink: 0 }} />
            <span id="code-viewer-title" style={{ fontFamily: 'var(--font-mono)', fontSize: '13px', fontWeight: 600, color: 'var(--color-ink)', overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>
              {filename}
            </span>
          </div>

          <div style={{ display: 'flex', alignItems: 'center', gap: '6px', flexShrink: 0 }}>
            {/* Copy Button */}
            <button
              onClick={handleCopy}
              style={{
                display: 'inline-flex',
                alignItems: 'center',
                gap: '5px',
                padding: '5px 9px',
                backgroundColor: copied ? 'rgba(34, 197, 94, 0.15)' : 'var(--color-surface-card)',
                color: copied ? '#4ade80' : 'var(--color-ink)',
                border: '1px solid var(--color-hairline)',
                borderRadius: 'var(--radius-xs)',
                fontSize: '11.5px',
                fontWeight: 500,
                cursor: 'pointer',
                transition: 'all 0.15s ease'
              }}
              aria-label="Copy code"
            >
              {copied ? <Check size={13} /> : <Copy size={13} />}
              <span className="code-action-label">{copied ? 'Copied!' : 'Copy'}</span>
            </button>

            {/* Download Button */}
            <button
              onClick={handleDownload}
              style={{
                display: 'inline-flex',
                alignItems: 'center',
                gap: '5px',
                padding: '5px 9px',
                backgroundColor: 'var(--color-surface-card)',
                color: 'var(--color-ink)',
                border: '1px solid var(--color-hairline)',
                borderRadius: 'var(--radius-xs)',
                fontSize: '11.5px',
                fontWeight: 500,
                cursor: 'pointer',
                transition: 'all 0.15s ease'
              }}
              aria-label="Download Python file"
            >
              <DownloadSimple size={13} />
              <span className="code-action-label">Download</span>
            </button>

            {/* Close Button */}
            <button
              onClick={onClose}
              style={{
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                padding: '6px',
                color: 'var(--color-mute)',
                backgroundColor: 'var(--color-surface-card)',
                border: '1px solid var(--color-hairline)',
                borderRadius: 'var(--radius-xs)',
                cursor: 'pointer'
              }}
              aria-label="Close code viewer"
            >
              <X size={16} />
            </button>
          </div>
        </div>

        {/* Code Content Area */}
        <div style={{ padding: '0', overflowY: 'auto', flex: 1, backgroundColor: 'var(--color-canvas)', WebkitOverflowScrolling: 'touch' }}>
          <pre
            className="language-python"
            style={{
              margin: 0,
              padding: '1rem 1.25rem',
              backgroundColor: 'transparent',
              fontSize: '13px',
              lineHeight: 1.6,
              overflowX: 'auto',
              WebkitOverflowScrolling: 'touch'
            }}
          >
            <code className="language-python" dangerouslySetInnerHTML={{ __html: highlightedHtml }} />
          </pre>
        </div>
      </div>

      <style>{`
        @media (max-width: 440px) {
          .code-action-label {
            display: none !important;
          }
        }
      `}</style>
    </div>
  );
};
