import React from 'react';
import { useData } from '../contexts/DataContext';

function VolumeBannerScroll() {
  const { data, loading } = useData();
  const volumeData = data.volume || [];

  if (loading && !volumeData.length) {
    return (
      <div className="py-4">
        <div className="text-center text-gray-400">Loading volume data...</div>
      </div>
    );
  }

  if (!volumeData.length) {
    return (
      <div className="py-4">
        <div className="text-center text-gray-400">No data available</div>
      </div>
    );
  }

  // Duplicate the data to create a seamless scrolling effect
  const displayData = [...volumeData, ...volumeData];

  return (
    <div className="overflow-hidden scroll-container-fade">
      <div className="flex items-center gap-6 animate-marquee whitespace-nowrap py-4">
        {displayData.map((item, idx) => (
          <a
            key={`${item.id}-${idx}`}
            href={item.url}
            target="_blank"
            rel="noopener noreferrer"
            className="inline-block bg-transparent px-5 py-2 min-w-[160px] text-center transition-all duration-300 ease-in-out flex-shrink-0 rounded-lg"
            style={{ border: 'none', boxShadow: 'none' }}
          >
            <div className="font-bold text-base">{item.id}</div>
            <div className="text-sm text-[--text-light]">${parseFloat(item.price).toFixed(2)}</div>
            <div className="text-xs font-bold" style={{ color: 'var(--primary-blue)' }}>
              Vol 24h: ${new Intl.NumberFormat('en-US', { notation: 'compact', compactDisplay: 'short' }).format(item.volume_24h)}
            </div>
          </a>
        ))}
      </div>
    </div>
  );
}

export default VolumeBannerScroll;