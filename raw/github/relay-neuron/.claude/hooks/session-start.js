/**
 * Session Start Hook for Relay Neuron Research Assistant
 *
 * This hook executes when a Claude Code session starts in the relay-neuron project.
 * It provides a summary of research progress, pending tasks, and quick commands.
 *
 * Format: CommonJS module (required by Claude Code hooks)
 */

const fs = require('fs');
const path = require('path');

// Project root directory
const PROJECT_ROOT = path.join(__dirname, '..', '..');

/**
 * Read a file safely, returning empty string if it doesn't exist
 */
function readFile(filepath) {
  try {
    return fs.readFileSync(filepath, 'utf8');
  } catch (e) {
    return '';
  }
}

/**
 * Extract task list items from RESEARCH_MASTER_LIST.md
 */
function parseTaskList(content) {
  const pending = [];
  const completed = [];

  const taskRegex = /-\s*\[([ x])\]\s*(.+?)(?:\s*\((\d{4}-\d{2}-\d{2})\))?/g;
  let match;

  while ((match = taskRegex.exec(content)) !== null) {
    const isDone = match[1] === 'x';
    const taskName = match[2].trim();
    const date = match[3] || null;

    if (isDone) {
      completed.push({ name: taskName, date });
    } else {
      pending.push({ name: taskName, date });
    }
  }

  return { pending, completed };
}

/**
 * Get list of recent research files
 */
function getRecentResearchFiles(limit = 10) {
  const researchDir = path.join(PROJECT_ROOT, 'research');

  try {
    const files = fs.readdirSync(researchDir)
      .filter(f => f.endsWith('.md'))
      .map(f => {
        const filepath = path.join(researchDir, f);
        const stats = fs.statSync(filepath);
        return { name: f, mtime: stats.mtime };
      })
      .sort((a, b) => b.mtime - a.mtime)
      .slice(0, limit);

    return files;
  } catch (e) {
    return [];
  }
}

/**
 * Format a date for display
 */
function formatDate(date) {
  if (!date) return 'No date';
  const d = new Date(date);
  return d.toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric' });
}

/**
 * Main hook function - called when session starts
 */
function onSessionStart() {
  console.log('\n========================================');
  console.log('  转接神经元 (Relay Neuron) Research Assistant');
  console.log('  Exercise Science Research Archive');
  console.log('========================================\n');

  // Read RESEARCH_MASTER_LIST.md
  const masterListPath = path.join(PROJECT_ROOT, 'RESEARCH_MASTER_LIST.md');
  const masterListContent = readFile(masterListPath);

  if (masterListContent) {
    const { pending, completed } = parseTaskList(masterListContent);

    console.log('--- Research Progress ---');
    console.log(`  Completed: ${completed.length} tasks`);
    console.log(`  Pending: ${pending.length} tasks`);

    if (pending.length > 0 && pending.length <= 10) {
      console.log('\n  Pending Tasks:');
      pending.forEach((task, i) => {
        const dateStr = task.date ? ` (${task.date})` : '';
        console.log(`    ${i + 1}. ${task.name}${dateStr}`);
      });
    } else if (pending.length > 10) {
      console.log('\n  Top 5 Pending Tasks:');
      pending.slice(0, 5).forEach((task, i) => {
        const dateStr = task.date ? ` (${task.date})` : '';
        console.log(`    ${i + 1}. ${task.name}${dateStr}`);
      });
      console.log(`    ... and ${pending.length - 5} more`);
    }
  }

  // Show recent research files
  const recentFiles = getRecentResearchFiles(5);
  if (recentFiles.length > 0) {
    console.log('\n--- Recent Research Files ---');
    recentFiles.forEach((file, i) => {
      const shortName = file.name.length > 50
        ? file.name.substring(0, 47) + '...'
        : file.name;
      const dateStr = formatDate(file.mtime);
      console.log(`  ${i + 1}. ${shortName}`);
    });
  }

  // Quick command suggestions
  console.log('\n--- Quick Commands ---');
  console.log('  • "Research [topic]" - Start new research on a topic');
  console.log('  • "Continue task X-X" - Work on specific task from list');
  console.log('  • "Search for [terms]" - Search literature database');
  console.log('  • "B-M-R-I write [topic]" - Write in B-M-R-I format');
  console.log('  • "Status" - Show detailed progress report');
  console.log('  • "Help rules" - Show core behavioral rules');

  console.log('\n========================================\n');

  return {
    context: {
      project: 'Relay Neuron',
      type: 'Exercise Science Research',
      researchDir: 'research/',
      rulesFile: '.claude/rules/exercise-research-core.md',
      skills: [
        'bri-structure',
        'citation-verification',
        'literature-search',
        'exercise-research-ideation',
        'study-quality-appraisal'
      ]
    }
  };
}

// Export for Claude Code hooks
module.exports = {
  onSessionStart
};

// If run directly (for testing), execute the hook
if (require.main === module) {
  onSessionStart();
}
