import React, { createContext, useState, useEffect, useContext } from 'react';
import axios from 'axios';

const DataContext = createContext(null);

export function DataProvider({ children }) {
  const [data, setData] = useState({
    banner: [],
    gainers: [],
    losers: [],
    volume: [],
  });
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [lastUpdated, setLastUpdated] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const res = await axios.get('/api/data');
        if (res.data.error) {
          // Handle cases where the API returns a 200 OK status but with an error message in the body
          throw new Error(res.data.error);
        }
        setData(res.data);
        setError(null);
        setLastUpdated(new Date());
      } catch (err) {
        const message = err.response?.data?.error || err.message || 'Failed to load data. The API might be down.';
        console.error('Failed to fetch market data:', message);
        setError(message);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
    // Refresh data every 15 seconds, the fastest required interval
    const interval = setInterval(fetchData, 15000);
    return () => clearInterval(interval);
  }, []);

  const value = { data, loading, error, lastUpdated };

  return <DataContext.Provider value={value}>{children}</DataContext.Provider>;
}

export const useData = () => {
  const context = useContext(DataContext);
  if (!context) {
    throw new Error('useData must be used within a DataProvider');
  }
  return context;
};
