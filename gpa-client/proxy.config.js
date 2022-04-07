const PROXY_CONFIG = [
  {
    context: ["/api/v1"],
    target: "http://localhost:5008",
    changeOrigin: true,
    secure: false,
  },
];

module.exports = PROXY_CONFIG;
