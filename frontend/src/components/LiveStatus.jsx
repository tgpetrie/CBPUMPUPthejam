import React from 'react';
import { useData } from '../contexts/DataContext';

function LiveStatus() {
  const { error, lastUpdated } = useData();
  const isLive = !error;

  return (
    <div className="mt-2 flex justify-center items-center gap-4 text-sm text-[--text-light] tracking-wide">
      <div className="flex items-center gap-1">
        <div
          className={`w-2.5 h-2.5 rounded-full ${
            isLive
              ? 'bg-[--primary-orange] animate-pulse shadow-lg shadow-[--primary-orange]/60'
              : 'bg-red-600'
          }`}
        />
        <span>{isLive ? 'LIVE' : 'OFFLINE'}</span>
      </div>
      {isLive && lastUpdated && (
        <div className="text-xs text-[--text-muted]">
          ⏱ Last updated: {lastUpdated.toLocaleTimeString()}
        </div>
      )}
    </div>
  );
}

export default LiveStatus;
    
  