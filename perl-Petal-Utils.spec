#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Petal
%define	pnam	Utils
Summary:	Petal::Utils - Useful template modifiers for Petal.
#Summary(pl):	
Name:		perl-Petal-Utils
Version:	0.06
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/W/WM/WMCKEE/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d93d4e1724a967891b4974b6985986cb
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Date::Format) >= 0.01
BuildRequires:	perl(Petal) >= 1.06
BuildRequires:	perl(URI::Escape) >= 3.0
BuildRequires:	perl(Module::Build) >= 0.20
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Petal::Utils package contains commonly used Petal modifiers (or plugins),
and bundles them with an easy-to-use installation interface. 

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes INSTALL README TODO
%{perl_vendorlib}/Petal/*.pm
%{perl_vendorlib}/Petal/Utils
%{_mandir}/man3/*
