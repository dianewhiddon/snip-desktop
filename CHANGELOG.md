# Changelog

## 0.1.3 — 2026-10-25

- Full web page reads the browser address on the first try. Chrome, Edge and Brave expose the page address to Windows accessibility only after a reader first connects, so 0.1.2's single lookup usually missed and asked for the URL. Snip now retries within its five-second limit; a typical lookup takes about a second. Still no keystrokes and no clipboard access.
- The address test now launches Chrome without forcing accessibility on, matching real use; it fails on 0.1.2 and passes on 0.1.3.
- Release checks add an install from the published download on a PC with consumer antivirus protection on.

## 0.1.2 — 2026-10-23

Security update. Install it in place of 0.1.1.

- Pillow 12.3.0 → 13.0.0, fixing its critical and high image-decoding advisories.
- Development tools: certifi 2026.7.22 → 2026.10.19 (removes the distrusted emSign roots) and uv 0.13.1 → 0.13.4.
- No change to capture, save, clipboard, shortcut or installer behavior.

## 0.1.1 — 2026-10-16

- Apply the shared gold action and light-gold accent palette on neutral gray surfaces.
- Separate action, selection and focus colors; preserve native controls and workflows.
- Refresh design documentation and release screenshots. Dependencies and installation behavior are unchanged.


## 0.1.0 — 2026-10-15

First public Windows source release.

- Region, desktop, active-window, scrolling and full-page web captures.
- Neutral grayscale interface with teal controls and blue annotation marks.
- Arrow, box, blur and opaque pixel-redaction tools; every edit saves a new PNG.
- Keyboard-accessible capture menu and explicit URL fallback.
- Read-only browser-address lookup that preserves the clipboard.
- One active session, bounded captures, atomic saves and validated local configuration.
- Isolated Python environment and Chromium installation; optional startup shortcuts.
- Hashed dependency locks, regression tests, Windows CI and documented release checks.
