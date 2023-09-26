#This file is only in agehring/primaire feature/SecurityIssue1

def _SendTemplateResponseAMG(self, filename, specials, params,
                            new_cookie_text=None):
    """Sends a response using a gtl template.

    Args:
      filename: The template file.
      specials: Other special values for this request.
      params: Cgi parameters.
      new_cookie_text: New cookie to set.
    """
    f = None
    try:
      f = _Open(RESOURCE_PATH, filename)
      template = f.read()
    finally:
      if f: f.close()
    self._SendHtmlResponse(
        gtl.ExpandTemplate(template, specials, params),
        new_cookie_text)
