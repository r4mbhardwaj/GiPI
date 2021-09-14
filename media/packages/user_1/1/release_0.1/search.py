def search_result(text, *args, **kwargs):
    res = wolframalpha_answer(text=text, *args, **kwargs)
    if not res:
        res = google_results_embed(text, *args, **kwargs)
    return res