# CreativeFlow - Setup Configuration
# Use this file to document installation and setup procedures

## Installation Checklist

### Prerequisites
- [ ] Python 3.10+ installed
- [ ] Git installed (optional)
- [ ] Database server (optional - SQLite works out of the box)

### Initial Setup
- [ ] Clone or download repository
- [ ] Run install.sh (Linux/macOS) or install.bat (Windows)
- [ ] Verify .venv is created
- [ ] Verify dependencies are installed
- [ ] Verify UI files are compiled

### First Run
- [ ] Execute `python main.py`
- [ ] Login with default credentials or create admin user
- [ ] Configure company/empresa from admin panel
- [ ] Test database connection
- [ ] Configure database engine (SQLite/MariaDB/PostgreSQL)

### Development Setup
- [ ] Install development dependencies: `pip install -r requirements-dev.txt`
- [ ] Configure IDE (PyCharm, VS Code, etc.)
- [ ] Run tests: `pytest`
- [ ] Compile UI after changes: `./scripts/compile_ui.sh`

## Supported Platforms

### ✅ Linux
- Ubuntu 20.04+
- Debian 11+
- Fedora 35+
- Arch Linux
- Other distributions with Python 3.10+

### ✅ macOS
- macOS 11 (Big Sur) or later
- macOS 12 (Monterey)
- macOS 13 (Ventura)
- macOS 14 (Sonoma)

### ✅ Windows
- Windows 10 (build 19041+)
- Windows 11
- Windows Server 2019+

## Database Support

### SQLite (Default)
- No additional configuration required
- File: `creativeflow.db`
- Best for: Single user, development, small teams

### MariaDB/MySQL
- Requires MariaDB 10.5+ or MySQL 8.0+
- Configure from admin panel
- Best for: Multi-user, production environments

### PostgreSQL
- Requires PostgreSQL 12+
- Configure from admin panel
- Best for: Enterprise, high-volume data

## Troubleshooting

### Common Issues

**Python not found**
```bash
# Linux/macOS
which python3
python3 --version

# Windows
where python
python --version
```

**Permission denied on scripts**
```bash
# Linux/macOS
chmod +x install.sh
chmod +x scripts/compile_ui.sh
```

**PySide6 installation fails**
- Ensure you have build tools installed
- Linux: `sudo apt install python3-dev` (Ubuntu/Debian)
- macOS: Install Xcode Command Line Tools
- Windows: Install Visual C++ Build Tools

**Database connection fails**
- Verify database server is running
- Check credentials in empresa configuration
- Test connection using database client

**UI looks wrong/colors are off**
- Verify `styles.qss` exists
- Check that UI files were compiled: `./scripts/compile_ui.sh`
- Verify no hardcoded colors in custom widgets

## Performance Tips

1. **Use PostgreSQL or MariaDB for production**
   - SQLite is great for development but may be slower with multiple users

2. **Keep .venv on fast storage**
   - SSD recommended for better startup times

3. **Compile UI files after changes**
   - Run `./scripts/compile_ui.sh` after editing .ui files

4. **Monitor database size**
   - Regular backups recommended
   - Use database optimization tools

## Security Notes

- Change default admin password immediately
- Use strong passwords for database connections
- Keep Python and dependencies updated
- Backup database regularly
- Restrict database access to localhost when possible

## Support

For issues during installation:
1. Check this setup guide
2. Review README.md
3. Check logs in `logs/` directory
4. Report issues on GitHub

---
Last updated: 2026-01-11

