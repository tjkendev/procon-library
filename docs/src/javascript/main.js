window.onload = () => {
  // add buttons for copying code to clipboard
  $(".listingblock").each((i, e) => {
    const $el = $(e)
    const $code = $el.find("code")
    $code.addClass(`code-idx-${i}`)
    $el.prepend(`<button type="button" class="copy-btn" data-clipboard-target=".code-idx-${i}">Copy to clipboard</button>`)
    new ClipboardJS('.copy-btn');
  });
}