# revision 25030
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-latex
Epoch:		1
Version:	20120224
Release:	1
Summary:	Basic LaTeX packages
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-latex.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-collection-basic
Requires:	texlive-ae
Requires:	texlive-amscls
Requires:	texlive-amsmath
Requires:	texlive-babel
Requires:	texlive-babelbib
Requires:	texlive-carlisle
Requires:	texlive-colortbl
Requires:	texlive-fancyhdr
Requires:	texlive-fix2col
Requires:	texlive-geometry
Requires:	texlive-graphics
Requires:	texlive-hyperref
Requires:	texlive-latex
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
Requires:	texlive-tools

%description
These packages are mandated by the core LaTeX team, or at least
very strongly recommended.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install