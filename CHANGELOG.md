# Changelog

## 0.1.5 — 2026-11-03

Windows interaction and shutdown reliability.

- The web-address dialog sizes to its contents so its buttons remain visible at 200% display scaling.
- A selected capture retains the session while waiting for the menu to disappear; another action or Quit cannot interrupt that interval.
- Quit signals the native shortcut thread and keeps Tk responsive until a pending callback finishes, avoiding the join/GUI wait cycle.
- Added actual initialized-window dispatch/shutdown coverage and matched desktop fixtures to the application's DPI mode.

## 0.1.4 — 2026-11-03

Battery.

- Snip's window no longer looks for work 25 times a second. It sleeps until something is posted to it, with a slow 4-per-second safety check, so the processor can sleep between uses. Idle use measured on the maintainer's laptop with the personal edition of the same change fell from about 0.39% to about 0.08% of one processor core.
- No change to the Ctrl+Shift+S shortcut (it already waited for Windows without polling), capture, annotation, saving, the clipboard or the installer.

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
