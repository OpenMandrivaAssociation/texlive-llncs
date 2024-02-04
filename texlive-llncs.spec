Name:		texlive-llncs
Version:	69629
Release:	1
Summary:	Document class and bibliography style for Lecture Notes in Computer Science (LNCS)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/llncs
License:	cc-by-4
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/llncs.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/llncs.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is Springer's official macro package for typesetting
contributions to be published in Springer's Lecture Notes in
Computer Science (LNCS) and its related proceedings series
CCIS, LNBIP, LNICST, and IFIP AICT.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/llncs
%{_texmfdistdir}/bibtex/bst/llncs
%doc %{_texmfdistdir}/doc/latex/llncs

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
