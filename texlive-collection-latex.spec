Name:		texlive-collection-latex
Epoch:		1
Version:	69131
Release:	2
Summary:	LaTeX fundamental packages
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-latex.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-collection-basic
Requires:	texlive-ae
Requires:	texlive-amscls
Requires:	texlive-amsmath
Requires:	texlive-babel
Requires:	texlive-babel-english
Requires:	texlive-babelbib
Requires:	texlive-carlisle
Requires:	texlive-colortbl
Requires:	texlive-fancyhdr
Requires:	texlive-fix2col
Requires:	texlive-geometry
Requires:	texlive-graphics
Requires:	texlive-hyperref
Requires:	texlive-latex
Requires:	texlive-latex-bin
Requires:	texlive-latex-fonts
Requires:	texlive-latexconfig
Requires:	texlive-ltxmisc
Requires:	texlive-mfnfss
Requires:	texlive-mptopdf
Requires:	texlive-natbib
Requires:	texlive-oberdiek
Requires:	texlive-pdftex-def
Requires:	texlive-pslatex
Requires:	texlive-psnfss
Requires:	texlive-pspicture
Requires:	texlive-tex-ini-files
Requires:	texlive-tools
Requires:	texlive-url

%description
These packages are either mandated by the core LaTeX team, or
very widely used and strongly recommended in practice.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c

%build

%install
