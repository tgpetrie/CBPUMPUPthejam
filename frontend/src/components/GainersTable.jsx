import React from 'react';
import { useData } from '../contexts/DataContext';

function GainersTable() {
  const { data } = useData();
  const gainersData = data.gainers || [];

  return (
    <div className="bg-[--glass-bg] rounded-2xl p-4 shadow-xl shadow-[--primary-blue]/30 border border-[--glass-border] backdrop-blur-md">
      <h2 className="text-lg font-extrabold text-[--primary-blue] mb-2 tracking-wide">Top Gainers (3min)</h2>
      <ul className="space-y-1">
        {gainersData.length > 0 ? (
          gainersData.map((item, i) => (
            <li key={item.id}>
              <a
                href={item.url}
                target="_blank"
                rel="noopener noreferrer"
                className="flex justify-between items-center text-sm text-[--text-light] p-3 rounded-lg transition-all duration-200 bg-white/5 hover:bg-white/10 border border-transparent hover:border-[--primary-blue] hover:shadow-[0_0_16px_0_var(--primary-blue)] hover:scale-[1.025] focus:scale-[1.025] focus:shadow-[0_0_20px_0_var(--primary-blue)] outline-none"
                style={{ boxShadow: '0 1px 8px 0 rgba(0,191,255,0.08)' }}
              >
                <span className="font-bold text-[--text-white] text-base">{i + 1}. {item.id}</span>
                <span className="font-semibold text-base" style={{ color: 'var(--primary-blue)' }}>
                  +{parseFloat(item.change_3m).toFixed(2)}%
                </span>
              </a>
            </li>
          ))
        ) : (
          <li className="text-center text-sm text-[--text-muted] py-4">No gainers data available.</li>
        )}
      </ul>
    </div>
  );
}

export default GainersTable;

