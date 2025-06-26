import React from 'react';
import { useData } from '../contexts/DataContext';

function TopBannerScroll() {
  const { data, loading } = useData();
  const bannerData = data.banner || [];

  if (loading && !bannerData.length) return <div className="text-center text-gray-400 py-4">Loading top movers...</div>;
  if (!bannerData.length) return <div className="text-center text-gray-400 py-4">No data available</div>;

  // Duplicate the data to create a seamless scrolling effect
  const displayData = [...bannerData, ...bannerData];

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
            <div className="text-sm font-bold" style={{ color: 'var(--primary-blue)' }}>
              {parseFloat(item.change_1h) >= 0 ? '+' : ''}{parseFloat(item.change_1h).toFixed(2)}%
            </div>
          </a>
        ))}
      </div>
    </div>
  );
}

export default TopBannerScroll;
