%global packname  denstrip
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          1.5.2
Release:          1
Summary:          Density strips and other methods for compactly illustrating distributions
Group:            Sciences/Mathematics
License:          GPLv2+
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildArch:        noarch
Requires:         R-core



Requires:         R-survival R-vioplot R-lattice R-Hmisc 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex 

BuildRequires:   R-survival R-vioplot R-lattice R-Hmisc 
%description
Graphical methods for compactly illustrating probability distributions,
including density strips, density regions, sectioned density plots and
varying width strips.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
