#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	IP
%define	pnam	Country
Summary:	IP::Country - fast lookup of country codes from IP addresses
Summary(pl):	IP::Country - szybkie okre¶lanie kodów pañstw na podstawie adresu IP
Name:		perl-IP-Country
Version:	2.18
Release:	3
License:	Unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/authors/id/N/NW/NWETTERS/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9fc08c51555f2e81b042ca749af0eee8
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Geography-Countries
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Finding the home country of a client using only the IP address can be
difficult. Looking up the domain name associated with that address can
provide some help, but many IP address are not reverse mapped to any
useful domain, and the most common domain (.com) offers no help when
looking for country.

This module comes bundled with a database of countries where various
IP addresses have been assigned. Although the country of assignment
will probably be the country associated with a large ISP rather than
the client herself, this is probably good enough for most log analysis
applications, and under test has proved to be as accurate as
reverse-DNS and WHOIS lookup.

%description -l pl
Okre¶lanie kraju pochodzenia klienta przy u¿yciu samego adresu IP mo¿e
byæ trudne. Sprawdzanie nazwy domeny zwi±zanej z adresem mo¿e byæ
trochê pomocne, ale wiele adresów IP nie maj± odwrotnego odwzorowania
na ¿adn± u¿yteczn± domenê, a najpopularniejsza domena (.com) nie
pomaga w okre¶leniu kraju.

Ten modu³ jest dostarczany wraz z baz± danych krajów, do których
przypisano ró¿ne adresy IP. Choæ kraj przypisania bêdzie
prawdopodobnie krajem zwi±zanym raczej z du¿ym ISP ni¿ samym klientem,
jest to zwykle wystarczaj±ce do wiêkszo¶ci analiz logów aplikacji, a
testy dowiod³y, ¿e jest to tak samo dok³adne, jak odwzorowania
odwrotnego DNS i WHOIS.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES INSTALL README
%dir %{perl_vendorlib}/IP
%{perl_vendorlib}/IP/*.pm
%{perl_vendorlib}/IP/Country
%{_mandir}/man3/*
