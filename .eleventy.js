module.exports = function (eleventyConfig) {
  // Copy static assets (logos, certificate images/PDFs) straight through
  eleventyConfig.addPassthroughCopy("src/assets");

  // Extract the 11-char YouTube video ID from any link form
  // (watch?v=, youtu.be/, embed/, shorts/) or a bare ID.
  eleventyConfig.addFilter("youtubeId", (url) => {
    if (!url) return "";
    const s = String(url).trim();
    const m = s.match(/(?:v=|youtu\.be\/|embed\/|shorts\/)([\w-]{11})/);
    if (m) return m[1];
    if (/^[\w-]{11}$/.test(s)) return s;
    return s;
  });

  return {
    dir: {
      input: "src",
      output: "_site",
      data: "_data",
    },
    htmlTemplateEngine: "njk",
    markdownTemplateEngine: "njk",
  };
};
