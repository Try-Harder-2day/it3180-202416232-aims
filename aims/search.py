def search_by_title(dvd_list, keyword):
    return [dvd for dvd in dvd_list if keyword.lower() in dvd.title.lower()]
