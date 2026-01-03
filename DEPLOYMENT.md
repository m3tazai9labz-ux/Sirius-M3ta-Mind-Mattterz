# 🚀 Deployment Guide

## Quick Deployment Options

### Option 1: GitHub Pages (Recommended - Free)

1. Go to your repository settings
2. Navigate to "Pages" section
3. Select the branch: `copilot/create-landing-page-sirius-m3ta`
4. Select root directory `/`
5. Click "Save"
6. Your site will be live at: `https://m3tazai9labz-ux.github.io/Sirius-M3ta-Mind-Mattterz/`

### Option 2: Netlify (Free with Custom Domain)

1. Sign up at [netlify.com](https://netlify.com)
2. Click "Add new site" → "Import an existing project"
3. Connect your GitHub repository
4. Select branch: `copilot/create-landing-page-sirius-m3ta`
5. Build settings: Leave empty (static site)
6. Click "Deploy site"
7. Optional: Add custom domain in settings

### Option 3: Vercel (Free with Custom Domain)

1. Sign up at [vercel.com](https://vercel.com)
2. Click "New Project"
3. Import your GitHub repository
4. Select branch: `copilot/create-landing-page-sirius-m3ta`
5. Framework: None (static)
6. Click "Deploy"
7. Optional: Add custom domain in settings

### Option 4: Traditional Web Hosting

1. Download all files from the repository
2. Upload to your web hosting via FTP/SFTP:
   - `index.html`
   - `styles.css`
   - `script.js`
3. Ensure files are in the public_html or www directory
4. Visit your domain

## Post-Deployment Checklist

- [ ] Test all navigation links
- [ ] Test contact form
- [ ] Check mobile responsiveness
- [ ] Verify all sections display correctly
- [ ] Update contact information if needed
- [ ] Add Google Analytics (optional)
- [ ] Set up form backend/email integration
- [ ] Test on multiple browsers

## Connecting Contact Form to Backend

The contact form currently shows a success message client-side. To receive actual submissions:

### Option A: FormSpree (Easiest)

1. Sign up at [formspree.io](https://formspree.io)
2. Create a new form
3. Update the form in `script.js` (around line 95):

```javascript
fetch('https://formspree.io/f/YOUR_FORM_ID', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ name, email, service, message })
})
.then(response => response.json())
.then(data => {
    showFormResponse('Thank you! We will contact you soon.', 'success');
    contactForm.reset();
})
.catch(error => {
    showFormResponse('Sorry, something went wrong.', 'error');
});
```

### Option B: Email Service (Mailchimp, SendGrid, etc.)

Follow similar pattern to integrate with your preferred email service API.

### Option C: Custom Backend

Create your own backend endpoint and update the fetch URL accordingly.

## Adding Google Analytics (Optional)

Add this before the closing `</head>` tag in `index.html`:

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>
```

## Custom Domain Setup

After deploying, you can add a custom domain:

1. Purchase a domain from registrar (GoDaddy, Namecheap, etc.)
2. In your hosting platform (Netlify/Vercel/GitHub Pages):
   - Add custom domain in settings
   - Follow DNS configuration instructions
3. Update DNS records at your registrar
4. Wait for DNS propagation (up to 48 hours)

## SSL Certificate

All recommended hosting platforms (GitHub Pages, Netlify, Vercel) provide free SSL certificates automatically.

## Need Help?

Refer to the main README.md or contact the development team.
