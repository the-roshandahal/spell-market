var path = require("path");
var webpack = require("webpack");
var BundleTracker = require("webpack-bundle-tracker");

module.exports = {
  context: __dirname,
  entry: "./staticfiles/khalti/index.js",
  output: {
    path: path.resolve("./staticfiles/khalti/webpack_bundles/"),
    filename: "[name]-[hash].js",
  },
  mode: "production",
  plugins: [new BundleTracker({ filename: "./webpack-stats.json" })],
};
