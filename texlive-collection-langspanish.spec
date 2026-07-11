%global tl_name collection-langspanish
%global tl_revision 72203

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Spanish
Group:		Publishing
URL:		https://www.ctan.org/pkg/collection-langspanish
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-langspanish.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(antique-spanish-units)
Requires:	texlive(babel-catalan)
Requires:	texlive(babel-galician)
Requires:	texlive(babel-spanish)
Requires:	texlive(collection-basic)
Requires:	texlive(es-tex-faq)
Requires:	texlive(hyphen-catalan)
Requires:	texlive(hyphen-galician)
Requires:	texlive(hyphen-spanish)
Requires:	texlive(l2tabu-spanish)
Requires:	texlive(latex2e-help-texinfo-spanish)
Requires:	texlive(latexcheat-esmx)
Requires:	texlive(lshort-spanish)
Requires:	texlive(quran-es)
Requires:	texlive(texlive-es)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Support for Spanish.

