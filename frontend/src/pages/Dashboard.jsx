import { useState } from 'react';
import { scenarioAPI } from '../services/api';
import ScenarioDisplay from '../components/ScenarioDisplay';
import { DIFFICULTY_OPTIONS, LANGUAGE_OPTIONS } from '../utils/constants';
import './Dashboard.css';

export default function Dashboard() {
  const [skillTarget, setSkillTarget] = useState('');
  const [language, setLanguage] = useState('en');
  const [difficulty, setDifficulty] = useState('M01');
  const [scenario, setScenario] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleGenerate = async (e) => {
    e.preventDefault();
    setError('');
    setScenario(null);
    setLoading(true);

    try {
      const res = await scenarioAPI.generate({
        skill_target: skillTarget,
        language,
        difficulty,
      });
      setScenario(res.data);
    } catch (err) {
      setError(err.response?.data?.detail || 'Failed to generate scenario. Check your Groq API key.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="dashboard">
      <div className="dashboard-hero">
        <h2>Generate a Scenario</h2>
        <p>Enter any skill target and get an immersive Indian training scenario powered by Groq AI.</p>
      </div>

      <form className="generator-form glass" onSubmit={handleGenerate}>
        <div className="form-row">
          <div className="form-group flex-grow">
            <label htmlFor="skill">🎯 Skill Target</label>
            <input
              id="skill"
              type="text"
              value={skillTarget}
              onChange={(e) => setSkillTarget(e.target.value)}
              placeholder="e.g. Negotiation, Active Listening, Conflict Resolution..."
              required
              minLength={2}
            />
          </div>
        </div>

        <div className="form-row">
          <div className="form-group">
            <label htmlFor="language">🌐 Language</label>
            <select id="language" value={language} onChange={(e) => setLanguage(e.target.value)}>
              {LANGUAGE_OPTIONS.map((opt) => (
                <option key={opt.value} value={opt.value}>
                  {opt.label}
                </option>
              ))}
            </select>
          </div>
          <div className="form-group">
            <label htmlFor="difficulty">📊 Difficulty</label>
            <select id="difficulty" value={difficulty} onChange={(e) => setDifficulty(e.target.value)}>
              {DIFFICULTY_OPTIONS.map((opt) => (
                <option key={opt.value} value={opt.value}>
                  {opt.label}
                </option>
              ))}
            </select>
          </div>
        </div>

        {error && <p className="error-msg">{error}</p>}

        <button type="submit" className="btn btn-primary generate-btn" disabled={loading}>
          {loading ? (
            <>
              <span className="spinner" />
              Generating with Groq AI...
            </>
          ) : (
            <>⚡ Generate Scenario</>
          )}
        </button>
      </form>

      {loading && (
        <div className="loading-state glass">
          <div className="spinner" style={{ width: 40, height: 40 }} />
          <p>Creating your scenario with Llama 3.3 70B...</p>
        </div>
      )}

      {scenario && <ScenarioDisplay scenario={scenario} />}
    </div>
  );
}
