function addScrollEmptySpace() {
    var scrollableContainer = document.getElementById("scrollable-container");
    var scrollEmptySpace = document.getElementById("scroll-empty-space");
    //vertical scroll exists if content height is greater than heigth of the visible area 
    var hasVerticalScroll = scrollableContainer.scrollHeight > scrollableContainer.clientHeight;
    var scrolbarWidth = 0;
    //if scrollbar exists calculate its width
    if (hasVerticalScroll) {
      scrollbarWidth = scrollableContainer.offsetWidth - scrollableContainer.clientWidth;
    }
    //check if empty space has to be less than scrollbar width
    var emptySpace = scrollableContainer.offsetWidth - scrollableContainer.scrollWidth;
    if (scrollbarWidth > emptySpace) {
      scrollbarWidth = emptySpace;
    }
    scrollEmptySpace.style.minWidth = scrollbarWidth + 'px';
  }
  
  $(document).ready(function() {
    addScrollEmptySpace();
    window.addEventListener('resize', addScrollEmptySpace, false);
  });