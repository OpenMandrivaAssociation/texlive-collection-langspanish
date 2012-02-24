# revision 21528
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-langspanish
Version:	20120223
Release:	1
Summary:	Spanish
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-langspanish.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-hyphen-spanish
Requires:	texlive-hyphen-catalan
Requires:	texlive-hyphen-galician
Requires:	texlive-spanish
Requires:	texlive-spanish-mx
Requires:	texlive-collection-basic

%description
Support for typesetting Spanish.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
