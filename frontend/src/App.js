import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [formData, setFormData] = useState({
    icp_type: 'high_wage',
    milestone_code: 'M01',
    skill_target: '',
    language: 'en'
  });
  
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const icpTypes = [
    { value: 'high_wage', label: 'High Wage' },
    { value: 'low_wage', label: 'Low Wage' }
  ];

  const milestones = ['M01', 'M02', 'M03', 'M04', 'M05', 'M06', 'M07'];

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
    setError(null);
    setResult(null);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!formData.skill_target.trim()) {
      setError('Please enter a skill target');
      return;
    }
    
    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const response = await axios.post('http://localhost:8000/generate-scenario', formData);
      
      if (response.data.success) {
        setResult(response.data.data);
      } else {
        setError(response.data.error);
      }
    } catch (err) {
      setError('Failed to connect to server');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const renderRubric = (rubric) => {
    const axes = ['communication', 'composure', 'clarity', 'strategy', 'outcome'];
    return (
      <div className="rubric-container">
        <h3>Rubric</h3>
        <div className="rubric-grid">
          {axes.map(axis => (
            <div key={axis} className="rubric-item">
              <span className="rubric-label">{axis.toUpperCase()}</span>
              <div className="rubric-bar">
                <div 
                  className="rubric-fill" 
                  style={{ width: `${rubric[axis]}%`, backgroundColor: getScoreColor(rubric[axis]) }}
                >
                  <span className="rubric-score">{rubric[axis]}</span>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    );
  };

  const getScoreColor = (score) => {
    if (score >= 70) return '#4caf50';
    if (score >= 50) return '#ff9800';
    return '#f44336';
  };

  return (
    <div className="app">
      <header className="header">
        <h1>AI Scenario Writer</h1>
      </header>

      <div className="container">
        <div className="form-section">
          <form onSubmit={handleSubmit}>
            <div className="form-group">
              <label>User Type</label>
              <div className="icp-options">
                {icpTypes.map(type => (
                  <label key={type.value} className="icp-option">
                    <input
                      type="radio"
                      name="icp_type"
                      value={type.value}
                      checked={formData.icp_type === type.value}
                      onChange={handleChange}
                    />
                    <div className="icp-card">
                      {type.label}
                    </div>
                  </label>
                ))}
              </div>
            </div>

            <div className="form-row">
              <div className="form-group">
                <label>Milestone</label>
                <select name="milestone_code" value={formData.milestone_code} onChange={handleChange}>
                  {milestones.map(m => (
                    <option key={m} value={m}>{m}</option>
                  ))}
                </select>
              </div>

              <div className="form-group">
                <label>Language</label>
                <select name="language" value={formData.language} onChange={handleChange}>
                  <option value="en">English</option>
                  <option value="hi">Hindi</option>
                </select>
              </div>
            </div>

            <div className="form-group">
              <label>Skill Target</label>
              <input
                type="text"
                name="skill_target"
                value={formData.skill_target}
                onChange={handleChange}
                placeholder="Enter skill target"
                className="skill-input"
              />
            </div>

            <button type="submit" disabled={loading} className="generate-btn">
              {loading ? 'Generating...' : 'Generate Scenario'}
            </button>
          </form>
        </div>

        {error && (
          <div className="error-section">
            <div className="error-message">
              {error}
            </div>
          </div>
        )}

        {result && (
          <div className="result-section">
            <div className="scene-card">
              <h2>Scene</h2>
              <div className="scene-details">
                <p><strong>Setting:</strong> {result.scene.setting}</p>
                <p><strong>Time:</strong> {result.scene.time}</p>
                <p><strong>Context:</strong> {result.scene.context}</p>
              </div>
            </div>

            <div className="characters-card">
              <h2>Characters</h2>
              <div className="characters-grid">
                {result.characters.map((char, idx) => (
                  <div key={idx} className="character">
                    <div className="character-name">{char.name}</div>
                    <div className="character-role">{char.role}</div>
                    <div className="character-mood">{char.mood}</div>
                  </div>
                ))}
              </div>
            </div>

            <div className="antagonist-card">
              <h2>Antagonist Line</h2>
              <div className="antagonist-line">
                "{result.antagonist_opening_line}"
              </div>
            </div>

            <div className="strategies-card">
              <h2>Strategies</h2>
              <div className="strategies-grid">
                {result.strategy_chips.map((chip, idx) => (
                  <div key={idx} className="strategy-chip">
                    <div className="chip-label">{chip.label}</div>
                    <div className="chip-philosophy">{chip.philosophy}</div>
                  </div>
                ))}
              </div>
            </div>

            {renderRubric(result.rubric)}

            <div className="success-card">
              <h2>Success Criteria</h2>
              <ul>
                {result.success_criteria.map((criteria, idx) => (
                  <li key={idx}>{criteria}</li>
                ))}
              </ul>
            </div>

            <div className="transfer-card">
              <h2>Transfer Targets</h2>
              <div className="tags">
                {result.transfer_targets.map((target, idx) => (
                  <span key={idx} className="tag">{target}</span>
                ))}
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;