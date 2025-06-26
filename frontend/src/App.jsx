import './index.css';
import React from 'react';
import TopBannerScroll from './components/TopBannerScroll';
import GainersTable from './components/GainersTable';
import LosersTable from './components/LosersTable';
import VolumeBannerScroll from './components/VolumeBannerScroll';
import LiveStatus from './components/LiveStatus';
import bhabitLogo from './assets/bhabit-logo.png';
import { useData } from './contexts/DataContext';

function BannerSection({ title, children, isLargeTitle }) {
  return (
    <div className="max-w-7xl mx-auto px-4 mb-8">
      <div className="rounded-lg border border-[#222] bg-[#111] hover:shadow-orange-500/30 transition-shadow duration-500">
        <h2 className={`${isLargeTitle ? 'text-xl font-extrabold' : 'text-2xl font-bold'} tracking-tight text-white hover:drop-shadow-[0_0_10px_rgba(255,107,0,0.6)] transition duration-300 uppercase mb-4 text-center py-4`}>
          {title}
        </h2>
        {children}
      </div>
    </div>
  );
}

function App() {
  const { error } = useData();

  return (
    <div className="bg-black text-white min-h-screen font-sans">
      {error && (
        <div className="bg-red-600 text-white text-center p-2 font-bold shadow-lg" role="alert">
          API Error: {error}
        </div>
      )}

      {/* Header */}
      <header className="text-center py-8 px-4">
        <img src={bhabitLogo} alt="BHABIT Logo" className="mx-auto h-24 mb-2" />
        <h2 className="font-bold text-2xl tracking-widest uppercase" style={{ fontFamily: 'var(--font-stylized)' }}>
          Profits Buy Impulse
        </h2>
        <LiveStatus />
      </header>

      {/* Top banner */}
      <BannerSection title="1h Price Movers" isLargeTitle>
        <TopBannerScroll />
      </BannerSection>

      {/* Tables Container */}
      <div className="max-w-7xl mx-auto px-4 mt-6 mb-8 grid grid-cols-1 lg:grid-cols-2 gap-8">
        <div className="rounded-xl border border-[#222] bg-[#111] hover:shadow-orange-500/30 transition-shadow duration-500 p-6 shadow-inner shadow-black/30">
          <GainersTable />
        </div>
        <div className="rounded-xl border border-[#222] bg-[#111] hover:shadow-orange-500/30 transition-shadow duration-500 p-6 shadow-inner shadow-black/30">
          <LosersTable />
        </div>
      </div>

      {/* Volume banner */}
      <BannerSection title="1h Volume Leaders" isLargeTitle>
        <VolumeBannerScroll />
      </BannerSection>
    </div>
  );
}

export default App;