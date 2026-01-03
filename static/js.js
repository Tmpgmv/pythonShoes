$('#id_stock, #id_supplier').on('change', function() {
        $('#search-sort-filter').submit();
    });


$('#id_search').on('keyup', function() {
        $('#search-sort-filter').submit();
});