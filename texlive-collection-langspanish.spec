# revision 30372
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-langspanish
Epoch:		1
Version:	20180303
Release:	3
Summary:	Spanish
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-langspanish.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-collection-basic
Requires:	texlive-babel-catalan
Requires:	texlive-babel-galician
Requires:	texlive-babel-spanish
Requires:	texlive-es-tex-faq
Requires:	texlive-hyphen-catalan
Requires:	texlive-hyphen-galician
Requires:	texlive-hyphen-spanish
Requires:	texlive-l2tabu-spanish
Requires:	texlive-latex2e-help-texinfo-spanish
Requires:	texlive-latexcheat-esmx
Requires:	texlive-lshort-spanish
Requires:	texlive-spanish-mx

%description
Support for Spanish.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
