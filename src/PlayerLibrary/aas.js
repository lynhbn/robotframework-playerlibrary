function queryAll(document, label) {
   let xpath = '//label[text()="${label}"]/following-sibling::*[1]'
   let results = [];
   if (document.evaluate(xpath, document, null,
   XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.tagName == "DIV") {
      xpath += "/input";
   };
   let query = document.evaluate(xpath, document,
       null, XPathResult.ORDERED_NODE_SNAPSHOT_TYPE, null);
   for (let i = 0, length = query.snapshotLength; i < length; ++i) {
       results.push(query.snapshotItem(i));
   }
   return results;
       }