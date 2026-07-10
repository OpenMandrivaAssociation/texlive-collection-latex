%global tl_name collection-latex
%global tl_revision 78733

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	LaTeX fundamental packages
Group:		Publishing
URL:		https://www.ctan.org/pkg/collection-latex
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-latex.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Requires:	texlive(ae)
Requires:	texlive(amscls)
Requires:	texlive(amsmath)
Requires:	texlive(atbegshi)
Requires:	texlive(atveryend)
Requires:	texlive(auxhook)
Requires:	texlive(babel)
Requires:	texlive(babel-english)
Requires:	texlive(babelbib)
Requires:	texlive(bigintcalc)
Requires:	texlive(bitset)
Requires:	texlive(bookmark)
Requires:	texlive(carlisle)
Requires:	texlive(collection-basic)
Requires:	texlive(colortbl)
Requires:	texlive(epstopdf-pkg)
Requires:	texlive(etexcmds)
Requires:	texlive(etoolbox)
Requires:	texlive(fancyhdr)
Requires:	texlive(firstaid)
Requires:	texlive(fix2col)
Requires:	texlive(geometry)
Requires:	texlive(gettitlestring)
Requires:	texlive(graphics)
Requires:	texlive(graphics-cfg)
Requires:	texlive(grfext)
Requires:	texlive(hopatch)
Requires:	texlive(hycolor)
Requires:	texlive(hypcap)
Requires:	texlive(hyperref)
Requires:	texlive(intcalc)
Requires:	texlive(kvdefinekeys)
Requires:	texlive(kvoptions)
Requires:	texlive(kvsetkeys)
Requires:	texlive(l3backend)
Requires:	texlive(l3kernel)
Requires:	texlive(l3packages)
Requires:	texlive(latex)
Requires:	texlive(latex-bin)
Requires:	texlive(latex-fonts)
Requires:	texlive(latex-lab)
Requires:	texlive(latexconfig)
Requires:	texlive(letltxmacro)
Requires:	texlive(ltxcmds)
Requires:	texlive(ltxmisc)
Requires:	texlive(lua-uni-algos)
Requires:	texlive(mfnfss)
Requires:	texlive(mptopdf)
Requires:	texlive(natbib)
Requires:	texlive(oberdiek)
Requires:	texlive(pagesel)
Requires:	texlive(pdfescape)
Requires:	texlive(pdfmanagement)
Requires:	texlive(pdftexcmds)
Requires:	texlive(pslatex)
Requires:	texlive(psnfss)
Requires:	texlive(pspicture)
Requires:	texlive(refcount)
Requires:	texlive(rerunfilecheck)
Requires:	texlive(stringenc)
Requires:	texlive(tagpdf)
Requires:	texlive(tools)
Requires:	texlive(uniquecounter)
Requires:	texlive(url)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
These packages are either mandated by the core LaTeX team, or very
widely used and strongly recommended in practice.

%prep
%setup -q -c
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
