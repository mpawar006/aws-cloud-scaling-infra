# ─── Lightweight 15 MB Apache image ────────────────────────────────────────────
FROM httpd:2.4-alpine

# Copy everything in the repo (HTML + images + any CSS/JS) to the web root
COPY . /usr/local/apache2/htdocs/

# Expose port 80 (already the default for httpd)
EXPOSE 80
