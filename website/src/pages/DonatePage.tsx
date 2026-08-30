import React, { useEffect, useState } from 'react';
import QRCode from 'qrcode';
import { QrCode, Copy, Check, Heart, ShieldCheck } from '@phosphor-icons/react';

export const DonatePage: React.FC = () => {
  const [qrDataUrl, setQrDataUrl] = useState<string>('');
  const [copied, setCopied] = useState(false);
  const upiId = 'notdgx@upi';
  const upiUri = 'upi://pay?pa=notdgx@upi&pn=notdgx&cu=INR';

  useEffect(() => {
    QRCode.toDataURL(upiUri, {
      width: 260,
      margin: 1,
      color: {
        dark: '#ffffff',
        light: '#101010'
      }
    })
      .then(setQrDataUrl)
      .catch((err) => console.error('Failed to generate UPI QR:', err));
  }, [upiUri]);

  const handleCopy = async () => {
    try {
      await navigator.clipboard.writeText(upiId);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    } catch {
      setCopied(false);
    }
  };

  return (
    <div style={{ maxWidth: '800px', margin: '0 auto', padding: '48px 24px 80px', width: '100%' }}>
      <div style={{ textAlign: 'center', marginBottom: '40px' }}>
        <div
          style={{
            width: '48px',
            height: '48px',
            borderRadius: 'var(--radius-full)',
            backgroundColor: 'var(--color-surface-elevated)',
            display: 'inline-flex',
            alignItems: 'center',
            justifyContent: 'center',
            color: 'var(--color-ink)',
            marginBottom: '16px'
          }}
        >
          <Heart size={24} color="#f472b6" weight="fill" />
        </div>
        <h1 style={{ fontSize: '2.4rem', color: 'var(--color-ink)', marginBottom: '8px' }}>
          Support python-learning
        </h1>
        <p style={{ fontSize: '15px', color: 'var(--color-mute)', maxWidth: '540px', margin: '0 auto' }}>
          This project is an open, high-quality technical repository developed to provide clean, deep Python learning for developers worldwide.
        </p>
      </div>

      {/* Donation Card */}
      <div
        className="surface-card"
        style={{
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          textAlign: 'center',
          padding: '36px 24px',
          maxWidth: '480px',
          margin: '0 auto'
        }}
      >
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '16px', color: 'var(--color-ink)', fontSize: '16px', fontWeight: 600 }}>
          <QrCode size={20} />
          <span>UPI Instant Payment</span>
        </div>

        {/* QR Code Container */}
        <div
          style={{
            padding: '16px',
            backgroundColor: 'var(--color-surface-elevated)',
            border: '1px solid var(--color-hairline)',
            borderRadius: 'var(--radius-lg)',
            marginBottom: '20px',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center'
          }}
        >
          {qrDataUrl ? (
            <img
              src={qrDataUrl}
              alt="UPI QR Code"
              style={{ width: '220px', height: '220px', display: 'block', borderRadius: 'var(--radius-sm)' }}
            />
          ) : (
            <div style={{ width: '220px', height: '220px', display: 'flex', alignItems: 'center', justifyContent: 'center', color: 'var(--color-mute)' }}>
              Generating QR...
            </div>
          )}
        </div>

        {/* UPI ID Box */}
        <div
          style={{
            width: '100%',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'space-between',
            padding: '10px 14px',
            backgroundColor: 'var(--color-surface-card)',
            border: '1px solid var(--color-hairline)',
            borderRadius: 'var(--radius-md)',
            marginBottom: '14px'
          }}
        >
          <code style={{ fontFamily: 'var(--font-mono)', fontSize: '14px', color: 'var(--color-ink)' }}>
            {upiId}
          </code>
          <button
            onClick={handleCopy}
            style={{
              display: 'inline-flex',
              alignItems: 'center',
              gap: '6px',
              padding: '6px 12px',
              backgroundColor: copied ? 'rgba(34, 197, 94, 0.15)' : 'var(--color-surface-elevated)',
              color: copied ? '#4ade80' : 'var(--color-ink)',
              border: '1px solid var(--color-hairline)',
              borderRadius: 'var(--radius-xs)',
              fontSize: '12px',
              fontWeight: 500,
              cursor: 'pointer',
              transition: 'all 0.15s ease'
            }}
            aria-label="Copy UPI ID"
          >
            {copied ? <Check size={14} /> : <Copy size={14} />}
            <span>{copied ? 'Copied!' : 'Copy ID'}</span>
          </button>
        </div>

        <div style={{ display: 'flex', alignItems: 'center', gap: '6px', color: 'var(--color-ash)', fontSize: '12px' }}>
          <ShieldCheck size={16} />
          <span>Zero fee direct payment via GPay, PhonePe, Paytm, or BHIM.</span>
        </div>
      </div>
    </div>
  );
};
