import './ScenarioDisplay.css';

export default function ScenarioDisplay({ scenario }) {
  if (!scenario) return null;

  const { content, language, difficulty, skill_target } = scenario;
  const isHindi = language === 'hi';

  return (
    <div className={`scenario-display glass fade-in ${isHindi ? 'hindi' : ''}`}>
      <div className="scenario-meta">
        <span className="meta-badge">{difficulty}</span>
        <span className="meta-badge lang">{isHindi ? 'हिंदी' : 'English'}</span>
        <span className="meta-skill">{skill_target}</span>
      </div>

      <section className="scenario-section">
        <h3>📍 Scene</h3>
        <p>{content.scene}</p>
      </section>

      <section className="scenario-section">
        <h3>👥 Characters</h3>
        <ul>
          {content.characters.map((char, i) => (
            <li key={i}>{char}</li>
          ))}
        </ul>
      </section>

      <section className="scenario-section antagonist">
        <h3>⚡ Antagonist Line</h3>
        <blockquote>"{content.antagonist_line}"</blockquote>
      </section>

      <section className="scenario-section">
        <h3>💡 Strategy Chips</h3>
        <div className="strategy-grid">
          {content.strategy_chips.map((chip, i) => (
            <div key={i} className="strategy-chip">
              <span className="chip-label">{chip.label}</span>
              <p className="chip-approach">{chip.approach}</p>
              <p className="chip-explanation">{chip.explanation}</p>
            </div>
          ))}
        </div>
      </section>

      <section className="scenario-section">
        <h3>📊 Rubric</h3>
        <div className="rubric-grid">
          {content.rubric.map((item, i) => (
            <div key={i} className="rubric-item">
              <div className="rubric-header">
                <span className="rubric-criterion">{item.criterion}</span>
                <span className="rubric-score">{item.score}/5</span>
              </div>
              <p>{item.description}</p>
            </div>
          ))}
        </div>
      </section>

      <section className="scenario-section">
        <h3>✅ Success Criteria</h3>
        <ul className="check-list">
          {content.success_criteria.map((item, i) => (
            <li key={i}>{item}</li>
          ))}
        </ul>
      </section>

      <section className="scenario-section">
        <h3>🎯 Transfer Targets</h3>
        <ul className="transfer-list">
          {content.transfer_targets.map((item, i) => (
            <li key={i}>{item}</li>
          ))}
        </ul>
      </section>
    </div>
  );
}
