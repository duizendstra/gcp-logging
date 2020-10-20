const functions = require('firebase-functions');

exports.firebase = functions
    .region('europe-west3')
    .https.onRequest((req, res) => {
        functions.logger.warn(`firebase warn`);
        return res.status(201).send();
});