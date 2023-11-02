# Securing your Package Ecosystem with Trusted Publishing

* Presented at: PackagingCon 2023
* Presented by: William Woodruff

This talk will provide a developer-minded introduction to "trusted publishing," an OpenID Connect-based authentication scheme that PyPI has successfully deployed to reduce the need for (and risk associated with) manual configured API tokens. Thousands of packages (including many of Python's most critical packages) have already enrolled in trusted publishing, improving the overall security posture (and audibility) of the Python ecosystem.

We will cover trusted publishing in two parts: the first part will be a high-level overview of the trusted publishing scheme and how it uses ephemeral OpenID Connect credentials, including motivation for the scheme's security properties and how they improve upon pre-existing package index authentication schemes (e.g. user/password pairs and long-lived API tokens).

The second part will dive into the nitty-gritty details of how trusted publishing was implemented on PyPI, and will serve as both a retrospective on the work and a reference for other package indices considering similar models: it will cover some of the challenges posted by OIDC (including support for multiple identity providers), threat model considerations, as well as "knock-on" benefits (such as future adjoiners with code-signing schemes like Sigstore).
