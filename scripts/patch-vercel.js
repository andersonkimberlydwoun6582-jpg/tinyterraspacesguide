// Patch os.hostname() to use ASCII for Vercel CLI
const os = require('os');
const originalHostname = os.hostname;
os.hostname = () => 'ttsguide-pc';
console.log('Patched os.hostname():', originalHostname(), '->', os.hostname());

// Now require and run the Vercel CLI
const vercelPath = require.resolve('vercel');
// We need to run vercel as a child process with the patched os module
// But since we can't easily patch a child process, let's try a different approach
// Just try to login
