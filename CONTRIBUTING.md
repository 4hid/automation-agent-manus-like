# Contributing to Automation Agent

Thank you for your interest in contributing to the Automation Agent project! This document provides guidelines and information for contributors.

## 🤝 How to Contribute

### Reporting Issues

1. **Search existing issues** first to avoid duplicates
2. **Use the issue templates** when available
3. **Provide detailed information** including:
   - Steps to reproduce the issue
   - Expected vs actual behavior
   - Environment details (OS, Python version, etc.)
   - Relevant logs or error messages

### Suggesting Features

1. **Check the roadmap** to see if the feature is already planned
2. **Open a feature request** with:
   - Clear description of the feature
   - Use cases and benefits
   - Possible implementation approach
   - Any relevant examples or mockups

### Code Contributions

#### Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/your-username/automation-agent-manus-like.git
   cd automation-agent-manus-like
   ```
3. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   pip install -e .[dev]
   ```

#### Development Workflow

1. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. **Make your changes** following the coding standards
3. **Add tests** for new functionality
4. **Run the test suite**:
   ```bash
   python -m pytest tests/
   ```
5. **Run code quality checks**:
   ```bash
   black automation_agent/
   flake8 automation_agent/
   mypy automation_agent/
   ```
6. **Commit your changes**:
   ```bash
   git add .
   git commit -m "feat: add your feature description"
   ```
7. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```
8. **Create a Pull Request** on GitHub

## 📝 Coding Standards

### Python Style Guide

- Follow **PEP 8** style guidelines
- Use **Black** for code formatting
- Use **type hints** for all function parameters and return values
- Write **docstrings** for all public functions and classes
- Keep line length to **88 characters** (Black default)

### Code Quality

- **Test coverage** should be maintained above 80%
- **No linting errors** from flake8
- **Type checking** must pass with mypy
- **Security** considerations for all external integrations

### Documentation

- **Update README.md** for user-facing changes
- **Add docstrings** for new functions and classes
- **Update API documentation** for interface changes
- **Include examples** for new features

## 🧪 Testing

### Running Tests

```bash
# Run all tests
python -m pytest

# Run with coverage
python -m pytest --cov=automation_agent

# Run specific test file
python -m pytest tests/test_automation_agent.py

# Run with verbose output
python -m pytest -v
```

### Writing Tests

- **Unit tests** for individual functions and methods
- **Integration tests** for tool interactions
- **End-to-end tests** for complete workflows
- **Mock external dependencies** when appropriate
- **Test edge cases** and error conditions

### Test Structure

```python
import pytest
from automation_agent import AutomationAgent, Task, TaskType

class TestAutomationAgent:
    def test_agent_initialization(self):
        """Test agent initializes correctly."""
        agent = AutomationAgent()
        assert agent is not None
        assert len(agent.tasks) == 0
    
    def test_task_creation(self):
        """Test task creation and addition."""
        agent = AutomationAgent()
        task = Task("test", "Test task", TaskType.RESEARCH)
        agent.add_task(task)
        assert len(agent.tasks) == 1
```

## 🏗️ Architecture Guidelines

### Adding New Tools

1. **Inherit from BaseTool**:
   ```python
   from automation_agent.tools.base import BaseTool
   
   class NewTool(BaseTool):
       def __init__(self):
           super().__init__("new_tool", "Description of new tool")
       
       def execute(self, task: Task, context: dict) -> dict:
           # Implementation
           pass
   ```

2. **Register the tool** in the agent
3. **Add comprehensive tests**
4. **Update documentation**

### Adding New Task Types

1. **Extend TaskType enum**:
   ```python
   class TaskType(str, Enum):
       # ... existing types
       NEW_TYPE = "new_type"
   ```

2. **Implement execution method**:
   ```python
   def _execute_new_type_step(self, task: Task, state: State) -> Action:
       # Implementation
       pass
   ```

3. **Add to task execution mapping**
4. **Write tests and documentation**

## 📋 Pull Request Guidelines

### PR Requirements

- [ ] **Descriptive title** following conventional commits
- [ ] **Clear description** of changes and motivation
- [ ] **Tests added/updated** for new functionality
- [ ] **Documentation updated** as needed
- [ ] **Code quality checks** pass
- [ ] **No breaking changes** without major version bump

### PR Template

```markdown
## Description
Brief description of the changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Unit tests added/updated
- [ ] Integration tests added/updated
- [ ] Manual testing completed

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] Tests pass locally
```

### Review Process

1. **Automated checks** must pass
2. **Code review** by maintainers
3. **Testing** in development environment
4. **Approval** from at least one maintainer
5. **Merge** after all requirements met

## 🚀 Release Process

### Version Numbering

We follow **Semantic Versioning** (SemVer):
- **MAJOR**: Breaking changes
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes (backward compatible)

### Release Checklist

- [ ] Update version numbers
- [ ] Update CHANGELOG.md
- [ ] Create release notes
- [ ] Tag the release
- [ ] Build and publish packages
- [ ] Update documentation

## 💬 Communication

### Channels

- **GitHub Issues**: Bug reports and feature requests
- **GitHub Discussions**: General questions and ideas
- **Pull Requests**: Code review and collaboration

### Code of Conduct

- **Be respectful** and inclusive
- **Provide constructive feedback**
- **Help others learn and grow**
- **Focus on the code, not the person**

## 🎯 Areas for Contribution

### High Priority

- [ ] Enhanced error handling and recovery
- [ ] Performance optimizations
- [ ] Additional tool integrations
- [ ] Improved documentation

### Medium Priority

- [ ] Web UI development
- [ ] API enhancements
- [ ] Advanced scheduling features
- [ ] Plugin system

### Low Priority

- [ ] Additional output formats
- [ ] Internationalization
- [ ] Advanced analytics
- [ ] Cloud deployment options

## 📚 Resources

### Documentation

- [README.md](README.md) - Project overview
- [API Documentation](docs/api.md) - API reference
- [Examples](examples/) - Usage examples

### External Resources

- [Python Style Guide (PEP 8)](https://pep8.org/)
- [Conventional Commits](https://conventionalcommits.org/)
- [Semantic Versioning](https://semver.org/)

## 🙏 Recognition

Contributors will be recognized in:
- **CONTRIBUTORS.md** file
- **Release notes** for significant contributions
- **GitHub contributors** section

Thank you for contributing to the Automation Agent project! 🎉