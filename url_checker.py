from urllib.parse import urlparse


def analyze_url(url):
    result = {}

    parsed = urlparse(url)

    result["Scheme"] = parsed.scheme
    result["Domain"] = parsed.netloc
    result["Path"] = parsed.path

    warnings = []

    if parsed.scheme != "https":
        warnings.append("URL does not use HTTPS.")

    if "@" in url:
        warnings.append("URL contains '@', which can be suspicious.")

    if len(url) > 100:
        warnings.append("URL is unusually long.")

    if "-" in parsed.netloc:
        warnings.append("Domain contains hyphens; verify the domain carefully.")

    result["Warnings"] = warnings

    if warnings:
        result["Risk"] = "Potentially Suspicious"
    else:
        result["Risk"] = "No obvious indicators detected"

    return result
