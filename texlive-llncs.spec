%global tl_name llncs
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.26
Release:	%{tl_revision}.1
Summary:	Document class and bibliography style for Lecture Notes in Computer Science (...
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/llncs
License:	cc-by-4
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/llncs.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/llncs.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is Springer's official macro package for typesetting contributions
to be published in Springer's Lecture Notes in Computer Science (LNCS)
and its related proceedings series CCIS, LNBIP, LNICST, and IFIP AICT.

