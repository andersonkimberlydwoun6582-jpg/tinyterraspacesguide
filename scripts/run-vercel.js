const Module = require('module');
const originalLoad = Module._load;

// Patch os module before anything else uses it
Module._load = function(request, parent) {
    const exports = originalLoad.apply(this, arguments);
    if (request === 'os') {
        const origHostname = exports.hostname;
        exports.hostname = function() {
            return 'ttsguide-pc';
        };
    }
    return exports;
};

// Now run the Vercel CLI
require('C:\\Users\\86183\\AppData\\Roaming\\npm\\node_modules\\vercel\\dist\\index.js');
