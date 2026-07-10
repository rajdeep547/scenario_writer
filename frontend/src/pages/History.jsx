import { useEffect, useState } from 'react';
import { scenarioAPI } from '../services/api';
import ScenarioDisplay from '../components/ScenarioDisplay';
import './History.css';

export default function History() {
  const [scenarios, setScenarios] = useState([]);
  const [selected, setSelected] = useState(null);
  const [loading, setLoading] = useState(true);
  const [detailLoading, setDetailLoading] = useState(false);
  const [error, setError] = useState('');

  useEffect(() => {
    scenarioAPI
      .list()
      .then((res) => setScenarios(res.data))
      .catch(() => setError('Failed to load history'))
      .finally(() => setLoading(false));
  }, []);

  const handleSelect = async (id) => {
    setDetailLoading(true);
    setSelected(null);
    try {
      const res = await scenarioAPI.get(id);
      setSelected(res.data);
    } catch {
      setError('Failed to load scenario');
    } finally {
      setDetailLoading(false);
    }
  };

  if (loading) {
    return (
      <div className="history-loading">
        <div className="spinner" />
      </div>
    );
  }

  return (
    <div className="history">
      <div className="history-hero">
        <h2>Scenario History</h2>
        <p>Your previously generated scenarios</p>
      </div>

      {error && <p className="error-msg">{error}</p>}

      {scenarios.length === 0 ? (
        <div className="empty-state glass">
          <span>📭</span>
          <p>No scenarios yet. Generate your first one!</p>
        </div>
      ) : (
        <div className="history-layout">
          <div className="history-list glass">
            {scenarios.map((s) => (
              <button
                key={s.id}
                className={`history-item ${selected?.id === s.id ? 'active' : ''}`}
                onClick={() => handleSelect(s.id)}
              >
                <span className="item-skill">{s.skill_target}</span>
                <span className="item-meta">
                  {s.difficulty} · {s.language === 'hi' ? 'हिंदी' : 'EN'} ·{' '}
                  {new Date(s.created_at).toLocaleDateString()}
                </span>
              </button>
            ))}
          </div>

          <div className="history-detail">
            {detailLoading && (
              <div className="detail-loading glass">
                <div className="spinner" />
              </div>
            )}
            {selected && !detailLoading && <ScenarioDisplay scenario={selected} />}
            {!selected && !detailLoading && (
              <div className="detail-placeholder glass">
                <p>Select a scenario to view details</p>
              </div>
            )}
          </div>
        </div>
      )}
    </div>
  );
}
