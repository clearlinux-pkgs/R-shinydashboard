#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-shinydashboard
Version  : 0.7.2
Release  : 30
URL      : https://cran.r-project.org/src/contrib/shinydashboard_0.7.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/shinydashboard_0.7.2.tar.gz
Summary  : Create Dashboards with 'Shiny'
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+ MIT OFL-1.1
Requires: R-htmltools
Requires: R-promises
Requires: R-shiny
BuildRequires : R-htmltools
BuildRequires : R-promises
BuildRequires : R-shiny
BuildRequires : buildreq-R

%description
a theme on top of 'Shiny', making it easy to create attractive dashboards.

%prep
%setup -q -c -n shinydashboard
cd %{_builddir}/shinydashboard

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1633015903

%install
export SOURCE_DATE_EPOCH=1633015903
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library shinydashboard
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library shinydashboard
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library shinydashboard
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc shinydashboard || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/shinydashboard/AdminLTE/AdminLTE.css
/usr/lib64/R/library/shinydashboard/AdminLTE/AdminLTE.min.css
/usr/lib64/R/library/shinydashboard/AdminLTE/_all-skins.css
/usr/lib64/R/library/shinydashboard/AdminLTE/_all-skins.min.css
/usr/lib64/R/library/shinydashboard/AdminLTE/app.js
/usr/lib64/R/library/shinydashboard/AdminLTE/app.js.map
/usr/lib64/R/library/shinydashboard/AdminLTE/app.min.js
/usr/lib64/R/library/shinydashboard/AdminLTE/app.min.js.map
/usr/lib64/R/library/shinydashboard/AdminLTE/fonts/Source_Sans_Pro_300.ttf
/usr/lib64/R/library/shinydashboard/AdminLTE/fonts/Source_Sans_Pro_300italic.ttf
/usr/lib64/R/library/shinydashboard/AdminLTE/fonts/Source_Sans_Pro_400.ttf
/usr/lib64/R/library/shinydashboard/AdminLTE/fonts/Source_Sans_Pro_400italic.ttf
/usr/lib64/R/library/shinydashboard/AdminLTE/fonts/Source_Sans_Pro_600.ttf
/usr/lib64/R/library/shinydashboard/AdminLTE/fonts/Source_Sans_Pro_600italic.ttf
/usr/lib64/R/library/shinydashboard/AdminLTE/fonts/Source_Sans_Pro_700.ttf
/usr/lib64/R/library/shinydashboard/DESCRIPTION
/usr/lib64/R/library/shinydashboard/INDEX
/usr/lib64/R/library/shinydashboard/LICENSE
/usr/lib64/R/library/shinydashboard/Meta/Rd.rds
/usr/lib64/R/library/shinydashboard/Meta/features.rds
/usr/lib64/R/library/shinydashboard/Meta/hsearch.rds
/usr/lib64/R/library/shinydashboard/Meta/links.rds
/usr/lib64/R/library/shinydashboard/Meta/nsInfo.rds
/usr/lib64/R/library/shinydashboard/Meta/package.rds
/usr/lib64/R/library/shinydashboard/NAMESPACE
/usr/lib64/R/library/shinydashboard/NEWS.md
/usr/lib64/R/library/shinydashboard/R/shinydashboard
/usr/lib64/R/library/shinydashboard/R/shinydashboard.rdb
/usr/lib64/R/library/shinydashboard/R/shinydashboard.rdx
/usr/lib64/R/library/shinydashboard/help/AnIndex
/usr/lib64/R/library/shinydashboard/help/aliases.rds
/usr/lib64/R/library/shinydashboard/help/paths.rds
/usr/lib64/R/library/shinydashboard/help/shinydashboard.rdb
/usr/lib64/R/library/shinydashboard/help/shinydashboard.rdx
/usr/lib64/R/library/shinydashboard/html/00Index.html
/usr/lib64/R/library/shinydashboard/html/R.css
/usr/lib64/R/library/shinydashboard/shinydashboard.css
/usr/lib64/R/library/shinydashboard/shinydashboard.js
/usr/lib64/R/library/shinydashboard/shinydashboard.js.map
/usr/lib64/R/library/shinydashboard/shinydashboard.min.js
/usr/lib64/R/library/shinydashboard/shinydashboard.min.js.map
