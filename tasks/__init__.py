"""Collections of tasks for invoke."""
from invoke import Collection

from tasks import docs
from tasks import quality
from tasks import tests


namespace = Collection()
namespace.add_collection(docs)
namespace.add_collection(quality)
namespace.add_collection(tests)
